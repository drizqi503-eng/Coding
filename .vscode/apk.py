# Skrip Python untuk menampilkan informasi lagu So Far Away

lagu = {
    "judul": "So Far Away",
    "artis": "Avenged Sevenfold",
    "album": "Nightmare (2010)",
    "tema": "Duka cita dan penghormatan untuk sahabat yang telah berpulang.",
    "cuplikan_lirik": [
        "How do I live without the ones I loved?",
        "Time still turns the pages of the book it's burned",
        "Place and time always on my mind",
        "I have so much to say, but you're so far away",
    ],
}

print(f"=== {lagu['judul']} - {lagu['artis']} ===")
print(f"Album : {lagu['album']}")
print(f"Makna : {lagu['tema']}\n")
print("Cuplikan Lirik:")
for baris in lagu["cuplikan_lirik"]:
    print(f'  "{baris}"')