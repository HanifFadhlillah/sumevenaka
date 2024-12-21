import streamlit as st
import time
from matplotlib.figure import Figure

# Fungsi iteratif untuk menjumlahkan bilangan genap dari 1 hingga n
def sum_even_numbers_iterative(n):
    total = 0
    for i in range(2, n + 1, 2):  
        total += i
    return total

def sum_even_numbers_recursive_with_stack(n):
    stack = [(n, 0)]  # Simulate a recursive call stack (n, accumulator)
    result = 0

    while stack:
        current_n, accumulator = stack.pop()
        if current_n < 2:  # Basis kasus
            result = accumulator
        elif current_n % 2 == 0:  # Jika n adalah bilangan genap
            stack.append((current_n - 2, accumulator + current_n))
        else:  # Jika n adalah bilangan ganjil
            stack.append((current_n - 1, accumulator))

    return result

# Streamlit app
st.title("Perbandingan Algoritma Iteratif dan Rekursif")
st.write("""
Aplikasi ini membandingkan waktu eksekusi algoritma iteratif dan rekursif untuk menjumlahkan bilangan genap hingga `n`.
""")

# Input untuk nilai n
n = st.number_input("Masukkan nilai n (bilangan bulat positif):", min_value=1, value=10, step=1, format="%d")

if st.button("Hitung"):
    # Mengumpulkan data untuk berbagai nilai n
    n_values = list(range(2, n + 1, 2))  # Hanya bilangan genap
    iterative_times = []
    recursive_times = []

    for i in n_values:
        # Waktu eksekusi algoritma iteratif
        start_time_iterative = time.time()
        sum_even_numbers_iterative(i)
        iterative_times.append(time.time() - start_time_iterative)

        # Waktu eksekusi algoritma rekursif
        start_time_recursive = time.time()
        sum_even_numbers_recursive_with_stack(i)
        recursive_times.append(time.time() - start_time_recursive)

    # Menampilkan hasil akhir
    st.subheader("Hasil Perhitungan:")
    st.write(f"**Hasil Akhir (Iteratif):** {sum_even_numbers_iterative(n)}")
    st.write(f"**Hasil Akhir (Rekursif):** {sum_even_numbers_recursive_with_stack(n)}")

    # Membuat grafik perbandingan dalam bentuk garis
    st.subheader("Grafik Perbandingan Waktu Eksekusi:")
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    
    ax.plot(n_values, iterative_times, label="Iteratif", marker="o", color="blue")
    ax.plot(n_values, recursive_times, label="Rekursif", marker="o", color="green")
    ax.set_xlabel("Nilai n")
    ax.set_ylabel("Waktu Eksekusi (detik)")
    ax.set_title("Perbandingan Waktu Eksekusi Algoritma")
    ax.legend()

    # Menampilkan grafik
    st.pyplot(fig)
