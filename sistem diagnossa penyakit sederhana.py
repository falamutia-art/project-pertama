def input_gejala():
    print("=== INPUT GEJALA ===")
    data = {
        "demam": input("Apakah Anda mengalami demam? (ya/tidak): ").lower(),
        "tinggi": input("Apakah demam tinggi? (ya/tidak): ").lower(),
        "batuk": input("Apakah Anda mengalami batuk? (ya/tidak): ").lower(),
        "pilek": input("Apakah Anda mengalami pilek? (ya/tidak): ").lower(),
        "sesak": input("Apakah Anda mengalami sesak napas? (ya/tidak): ").lower()
    }
    return data


def diagnosa(gejala):
    # R2: COVID
    if (gejala["demam"] == "ya" and gejala["tinggi"] == "ya" and
        gejala["batuk"] == "ya" and gejala["sesak"] == "ya"):
        return "COVID"

    # R1: Flu
    elif (gejala["demam"] == "ya" and gejala["tinggi"] == "tidak" and
          gejala["batuk"] == "ya" and gejala["pilek"] == "ya"):
        return "Flu"

    # R3: Demam biasa
    elif (gejala["demam"] == "ya" and gejala["batuk"] == "tidak" and
          gejala["pilek"] == "tidak" and gejala["sesak"] == "tidak"):
        return "Demam biasa"

    # R4: Default
    else:
        return "Perlu pemeriksaan lanjut"


def main():
    print("=== SISTEM DIAGNOSA PENYAKIT ===")
    gejala = input_gejala()
    hasil = diagnosa(gejala)

    print("\n=== HASIL DIAGNOSA ===")
    print("Diagnosis:", hasil)


# Menjalankan program
main()