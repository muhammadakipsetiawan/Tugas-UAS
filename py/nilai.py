import texttable as tt

def nilai_mahasiswa():
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    nilai_akhir = []

    x = [[]]
    jawab = "y"
    tab = tt.Texttable()
    while (jawab == 'y'):
        print("\n=====================================================")
        nama.append(input("\n\tMasukan nama: "))
        nim.append(input("\tMaukan Nim: "))
        tugas = int(input("\tNilai tugas: "))
        tugas = float(tugas)
        nilai_tugas.append(tugas)
        uts = int(input("\tNilai uts: "))
        uts = float(uts)
        nilai_uts.append(uts)
        uas = int(input("\tNilai uas: "))
        uas = float(uas)
        nilai_uas.append(uas)
        hasil = (tugas+uts+uas)/3
        nilai_akhir.append(hasil)
        jawab = input("n\tTambah data [y/n]? ")

    for i in nama:
        idx = nama.index(i)
        x.append([idx+1,nama[idx],nim[idx],nilai_tugas[idx],nilai_uts[idx],nilai_uas[idx],nilai_akhir[idx]])
    tab.add_rows(x)
    tab.set_cols_align(['l','l','l','r','r','r','r'])
    tab.header(['no','nama','nim','nilai tugas','nilai uts','niali uas','nilai akhir'])
    print (tab.draw())
