def cari_pasangan(arr, target):
    terlihat = set()
    for angka in arr:
        komplemen = target - angka
        if komplemen in terlihat:
            return True
        terlihat.add(angka)
    return False

