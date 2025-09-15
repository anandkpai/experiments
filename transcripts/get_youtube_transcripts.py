from youtube_transcript_api import YouTubeTranscriptApi

video_id = "L4Bv3wAGpBA"

ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch(video_id, languages=['en'])

# transcript is a FetchedTranscript
print("Video:", transcript.video_id)
print("Language:", transcript.language, "(generated?" , transcript.is_generated, ")")

# Write plain transcript (no timestamps) to a file
with open("transcript.txt", "w", encoding="utf-8") as f:
    for snip in transcript:
        f.write(snip.text + "\n")

print("Transcript written to transcript.txt")