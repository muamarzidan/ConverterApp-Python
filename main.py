import tkinter as tk
from tkinter import messagebox


def konversi_string():
    input_string = input_text_ascii.get("1.0", "end-1c")
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
    hasil_ascii.delete("1.0", tk.END)
    hasil_ascii.insert("1.0", hasil_string)

def convert():
    input_str = input_string_sistem.get("1.0", "end-1c")
    option = opsi_dropdown.get()
    hasil = ""
    if input_str == "":
        messagebox.showerror("Error", "Input tidak boleh kosong")
    elif option == 'binary':
        binary = ''.join(format(ord(c), '08b') for c in input_str)  + " "
        label_hasil.delete("1.0", tk.END)
        label_hasil.insert("1.0", binary)
    elif option == 'hexadecimal':
        hexadecimal = ''.join(hex(ord(c))[2:] for c in input_str) + " "
        label_hasil.delete("1.0", tk.END)
        label_hasil.insert("1.0", hexadecimal)
    elif option == 'decimal':
        decimal = ''.join(str(ord(c)) for c in input_str) + " "
        label_hasil.delete("1.0", tk.END)
        label_hasil.insert("1.0", decimal)
    elif option == 'octal':
        octal = ''.join(oct(ord(c))[2:] for c in input_str) + " "
        label_hasil.delete("1.0", tk.END)
        label_hasil.insert("1.0", octal)
    else:
        messagebox.showerror("Error", "Salah memilih opsi")

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

Judul = tk.Label(window, text="Selamat datang di ConvertiN", font=("Poppins", 20), bg="#fff", fg="black")
Judul.pack()



#convert string ke ascii
label_judul = tk.Label(window, text="Convert String ke ascii", font=("Poppins", 12), bg="#263D42", fg="white")
label_judul.pack()
input_text_ascii = tk.Text(window, height=2, width=50)
input_text_ascii.pack()

conversion_var = tk.StringVar(value="hex")
asc_radiobutton = tk.Radiobutton(window, text="ASCII", variable=conversion_var, value="asc")
asc_radiobutton.config(width=20)
asc_radiobutton.pack(pady=10)

button_convert = tk.Button(window, text="Convert", command=konversi_string, bg="white", fg="black")
button_convert.pack()
button_convert.config(width=12)

hasil_ascii = tk.Text(window, height=2, width=50)
hasil_ascii.pack(pady=2)



#convert string ke sistem bilangan
label_judul = tk.Label(window, text="Convert String ke Sistem bilangan", font=("Poppins"), bg="#263D42", fg="white")
label_judul.pack(pady=1)

input_string_sistem = tk.Text(window, height=2, width=50)
input_string_sistem.pack(pady=1)

opsi_dropdown = tk.StringVar(window)
opsi_dropdown.set("Pilih sistem bilangan")
opsi_menu = tk.OptionMenu(window, opsi_dropdown, "binary", "hexadecimal", "decimal", "octal")
opsi_menu.config(width=20)
opsi_menu.pack(pady=5)

button_convert_str = tk.Button(window, text="Convert", command=convert)
button_convert_str.config(width=12)
button_convert_str.pack(pady=2)

label_hasil = tk.Text(window, height=2, width=50)
label_hasil.pack(pady=2)
# label_hasil = tk.Label(window, font=("Poppins", 10), height=1)
# label_hasil.pack(pady=1)



#convert bilangan
label_judul= tk.Label(window, text="Convert sistem bilangan", font=("Poppins"), bg="#263D42", fg="white")
label_judul.pack(pady=1)

input_angka = tk.Entry(window, font=("Poppins", 15), width=30)
input_angka.pack(pady=1)

label_pilihan = tk.Label(window, text="2: Binary | 8: Octal | 10: Decimal | 16: Hexadecimal", font=("Poppins", 10), bg="#263D42", fg="white")
label_pilihan.pack()

nilai_awal_input = tk.StringVar(value="Pilih Bilangan Awal")
opsi_dropdown_awal = tk.OptionMenu(window, nilai_awal_input, "2", "8", "10", "16")
opsi_dropdown_awal.config(width=20)
opsi_dropdown_awal.pack(padx=5) 

nilai_hasil_label = tk.Label(window, text="Pilih Akan Diconvert Ke", font=("Poppins"), bg="#263D42", fg="white")
nilai_hasil_label.pack()

nilai_hasil_input = tk.StringVar(value="Bilangan Akhir")
opsi_dropdown_akhir = tk.OptionMenu(window, nilai_hasil_input, "2", "8", "10", "16")
opsi_dropdown_akhir.config(width=20)
opsi_dropdown_akhir.pack(padx=5)

button_convert_bil = tk.Button(window, text="Convert", command=handle_konversi_basis,  width=15)
button_convert_bil.pack(pady=10)
button_convert_bil.config(width=12)

hasil = tk.Label(window, font=("Poppins", 10), height=1, bg="#ffffff", fg="black")
hasil.pack(pady=1)


window.mainloop()



