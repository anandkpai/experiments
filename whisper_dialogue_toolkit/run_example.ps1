param(
  [Parameter(Mandatory=$true)][string]$AudioPath,
  [string]$OutDir = "out",
  [string]$Model = "medium",
  [string]$Device = "auto",
  [double]$GapThreshold = 1.2,
  [int]$ChunkMinutes = 10,
  [string]$Speaker1 = "Anand",
  [string]$Speaker2 = "Anindya"
)

python transcript_whisper_local.py `
  --audio "$AudioPath" `
  --out_dir "$OutDir" `
  --model $Model `
  --device $Device `
  --gap_threshold $GapThreshold `
  --chunk_minutes $ChunkMinutes `
  --speaker1 "$Speaker1" `
  --speaker2 "$Speaker2"