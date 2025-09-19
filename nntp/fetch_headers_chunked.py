from create_db_for_ng import get_config, parse_overview_line
import nntp


def fetch_headers_chunked(config, group, limit: int, chunk_size: int = 500_000, newest_first: bool = True):
    """
    Fetch up to `limit` overview headers from `group` using XZVER in chunked ranges.
    Compression: XZVER returns gzipped data; read with _info_gzip.
    No post-slicing: we cap each XZVER range so total rows <= limit.

    Args:
        nntp_client: pynntp client (sync)
        group: NNTP group name
        limit: number of headers to fetch (<=0 means "all available")
        chunk_size: max articles per XZVER range (tune if server is touchy)
        newest_first: True → walk ranges from newest to oldest

    Returns:
        List[dict]: parsed overview rows
    """
    sconfig = config['servers']
    nntp_client = nntp.NNTPClient( sconfig['host'], sconfig['port'], sconfig['username'], sconfig['password'], use_ssl=True)


    count, first, last, name = nntp_client.group(group)
    first, last = int(first), int(last)
    print(f"Group: {name}, Articles: {count}, First: {first}, Last: {last}")

    enc = getattr(nntp_client, "encoding", "utf-8")
    want = (last - first + 1) if (limit is None or limit <= 0) else int(limit)
    got = 0
    rows = []

    if newest_first:
        hi = last
        lo = first
        while got < want and hi >= lo:
            # propose [start, end] going backwards
            end = hi
            start = max(lo, hi - chunk_size + 1)

            # tighten to remaining needed
            remaining = want - got
            if remaining < (end - start + 1):
                start = end - remaining + 1

            rng = f"{start}-{end}"
            code, msg = nntp_client.xzver(rng)
            # Expect: 224 ... [COMPRESS=GZIP]
            lines = nntp_client._info_gzip(code, msg)

            # decode + parse
            batch = [parse_overview_line(ln.decode(enc, "replace")) for ln in lines]
            rows.extend(batch)
            got += len(batch)

            # move window backward
            hi = start - 1

            # stop if server gave fewer than requested (we hit group start)
            if start == lo and len(batch) < (end - start + 1):
                break
    else:
        lo = first
        hi = last
        while got < want and lo <= hi:
            start = lo
            end = min(hi, lo + chunk_size - 1)

            remaining = want - got
            if remaining < (end - start + 1):
                end = start + remaining - 1

            rng = f"{start}-{end}"
            code, msg = nntp_client.xzver(rng)
            lines = nntp_client._info_gzip(code, msg)

            batch = [parse_overview_line(ln.decode(enc, "replace")) for ln in lines]
            rows.extend(batch)
            got += len(batch)

            lo = end + 1

            if end == hi and len(batch) < (end - start + 1):
                break

    print(f"Fetched {got} headers (limit={want}, chunk_size={chunk_size}, newest_first={newest_first})")
    return rows
