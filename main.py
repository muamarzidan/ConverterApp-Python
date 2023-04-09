import tkinter as tk
from tkinter import messagebox

def konversi_string():
    input_string = input_text.get("1.0", "end-1c")
    hasil_string = ""
    if input_string == "":
        messagebox.showerror("Error", "Input tidak boleh kosong")
        return
    elif conversion_var.get() == "asc":
        for char in input_string:
            hasil_string += str(ord(char)) + " "
    else:
        messagebox.showerror("Error", "Pilih tipe konversi dulu")
        return

    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", hasil_string)


def konversi_bilangan(nilai, basis):
    if basis == 2:
        return bin(nilai)[2:]
    elif basis == 8:
        return oct(nilai)[2:]
    elif basis == 10:
        return str(nilai)
    elif basis == 16:
        return hex(nilai)[2:]

def konversi_basis(basis, nilai_awal, nilai_hasil):
    try:
        if nilai_awal == nilai_hasil:
            return f"Hasilnya sama karena nilai awal dan akhir sama : {basis}"
        elif nilai_awal == 10:
            hasil_basis = int(basis)
        elif nilai_awal == 2:
            hasil_basis = int(basis, 2)
        elif nilai_awal == 8:
            hasil_basis = int(basis, 8)
        elif nilai_awal == 16:
            hasil_basis = int(basis, 16)
        
        if nilai_hasil == 10:
            return str(hasil_basis)
        else:
            return konversi_bilangan(hasil_basis, nilai_hasil)
    except ValueError:
        return f"Inputan anda yaitu {basis} tidak sesuai dengan basis data {nilai_awal}"

def handle_konversi_basis():
    basis = input_angka.get()
    nilai_awal = nilai_awal_input.get()
    nilai_hasil = nilai_hasil_input.get()
    if not basis:
        messagebox.showerror("Error", "Input tidak boleh kosong bro")
        return
    elif nilai_awal == "Pilih Bilangan":
        messagebox.showerror("Error", "Silahkan pilih bilangan mana yang mau dikonversi dulu")
        return
    try:
        nilai_awal = int(nilai_awal)
        nilai_hasil = int(nilai_hasil)
        if nilai_awal == nilai_hasil:
            hasil.config(text=f"Hasilnya sama karena nilai awal dan akhir sama: {basis}")
            return
        hasil_konversi = konversi_basis(basis, nilai_awal, nilai_hasil)
        hasil.config(text=f"Hasil konversi : {hasil_konversi}")
    except ValueError:
        messagebox.showerror("Error", f"Inputan anda yaitu {nilai_awal} atau {nilai_hasil} bukan angka")
        return


#mengconfigure GUI
window = tk.Tk()
window.configure(background='#263D42')
window.geometry("800x1000")
window.resizable(True, True)
window.title("CONVERTIN")

Judul = tk.Label(window, text="Selamat datang di ConvertiN", font=("Poppins", 30), bg="#fff", fg="black")
Judul.pack()

#convert string ke ascii
label_angka = tk.Label(window, text="Convert String ke ascii", font=("Poppins", 20), bg="#263D42", fg="white")
label_angka.pack(pady=5)
input_text = tk.Text(window, height=3, width=50)
input_text.pack()

conversion_var = tk.StringVar(value="hex")
asc_radiobutton = tk.Radiobutton(window, text="ASCII", variable=conversion_var, value="asc")
asc_radiobutton.pack(pady=10)

convert_button = tk.Button(window, text="Convert", command=konversi_string, bg="white", fg="black", width=15)
convert_button.pack()

output_text = tk.Text(window, height=3, width=50)
output_text.pack(pady=10)


#convert bilangan
label_angka= tk.Label(window, text="Convert bilangan", font=("Poppins", 20), bg="#263D42", fg="white")
label_angka.pack(pady=5)

input_angka = tk.Entry(window, font=("Poppins", 15), width=30)
input_angka.pack(pady=5)

label_pilihan = tk.Label(window, text="2: Binary | 8: Octal | 10: Decimal | 16: Hexadecimal", font=("Poppins", 10), bg="#263D42", fg="white")
label_pilihan.pack()

nilai_awal_input = tk.StringVar(value="Pilih Bilangan Awal")
nilai_awal_dropdown = tk.OptionMenu(window, nilai_awal_input, "2", "8", "10", "16")
nilai_awal_dropdown.pack(padx=10)

nilai_hasil_label = tk.Label(window, text="Pilih Akan Diconvert Ke", font=("Poppins", 14), bg="#263D42", fg="white")
nilai_hasil_label.pack(pady=2)

nilai_hasil_input = tk.StringVar(value="Bilangan Akhir")
nilai_hasil_dropdown = tk.OptionMenu(window, nilai_hasil_input, "2", "8", "10", "16")
nilai_hasil_dropdown.pack(padx=10)

angka_button = tk.Button(window, text="Convert", command=handle_konversi_basis,  width=15)
angka_button.pack(pady=10)

hasil = tk.Label(window, height=5)
hasil.pack(pady=10)

window.mainloop()



