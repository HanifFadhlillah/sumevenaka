import streamlit as st
import time
import matplotlib.pyplot as plt

# Fungsi iteratif untuk menjumlahkan bilangan genap dari 1 hingga n
def sum_even_numbers_iterative(n):
    total = 0
    for i in range(2, n + 1, 2):  
        total += i
    return total

# Fungsi rekursif dengan teknik Tail Recursion
def sum_even_numbers_tail_recursive(n, accumulator=0):
    if n < 2:  # Basis kasus, jika n lebih kecil dari 2, kembalikan hasil akumulator
        return accumulator
    if n % 2 == 0:  # Jika n adalah bilangan genap
        return sum_even_numbers_tail_recursive(n - 2, accumulator + n)
    else:  # Jika n adalah bilangan ganjil, lewati ke bilangan genap sebelumnya
        return sum_even_numbers_tail_recursive(n - 1, accumulator)

# Streamlit app
st.title("Perbandingan Algoritma Iteratif dan Rekursif")
st.write("""
Aplikasi ini membandingkan waktu eksekusi algoritma iteratif dan rekursif untuk menjumlahkan bilangan genap hingga `n`.
""")

# Input untuk nilai n
n = st.number_input("Masukkan nilai n (bilangan bulat positif):", min_value=1, value=10, step=1)

if st.button("Hitung"):
    # Waktu eksekusi algoritma iteratif
    start_time_iterative = time.time()
    result_iterative = sum_even_numbers_iterative(n)
    time_iterative = time.time() - start_time_iterative

    # Waktu eksekusi algoritma rekursif
    start_time_recursive = time.time()
    result_recursive = sum_even_numbers_tail_recursive(n)
    time_recursive = time.time() - start_time_recursive

    # Menampilkan hasil
    st.subheader("Hasil Perhitungan:")
    st.write(f"**Hasil (Iteratif):** {result_iterative}")
    st.write(f"**Hasil (Rekursif):** {result_recursive}")
    st.write(f"**Waktu Eksekusi (Iteratif):** {time_iterative:.6f} detik")
    st.write(f"**Waktu Eksekusi (Rekursif):** {time_recursive:.6f} detik")

    # Membuat grafik perbandingan
    st.subheader("Grafik Perbandingan Waktu Eksekusi:")
    algorithms = ["Iteratif", "Rekursif"]
    times = [time_iterative, time_recursive]

    fig, ax = plt.subplots()
    ax.bar(algorithms, times, color=["blue", "green"])
    ax.set_ylabel("Waktu Eksekusi (detik)")
    ax.set_title("Perbandingan Waktu Eksekusi Algoritma")
    st.pyplot(fig)
