import streamlit as st
import pandas as pd

from function import load_data, assesing_data, cleaning_data, merge_data_payment_order, merge_data_customer_order, create_plot_payment_popular, create_plot_cities_popular

# menambahkan header
# st.header('Orders, Payments, Customers E-Commerce Publik Dataset:sparkles:')
# judul web
st.title('Analisis Data Eksplorasi Pada Olist Departement Store Brazil Pada Tahun 2016 hingga 2018')

payments_df, customers_df, orders_df = load_data()

# hide menu
hide_menu = """
<style>
#MainMenu {
    visibility: hidden;
}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

st.write('Olist adalah platform e-commerce Brasil yang menghubungkan usaha kecil dan menengah dengan pelanggan di seluruh Brasil. Platform ini beroperasi sebagai pasar, tempat pedagang dapat mendaftarkan produk dan layanan mereka dan pelanggan dapat menelusuri dan membelinya secara online.')

st.subheader('Deskripsi Data Set')
st.write('Dataset yang digunakan adalah dataset customers, orders, dan payments')

st.subheader('Pertanyaan Bisnis')
st.write('1.  Metode pembayaran manakah yang paling umum digunakan pelanggan Olist Departement Store ?')
st.write('2.  Darimanakah kota asal dengan populasi terbesar pelanggan Olist Departement Store ? ')

st.subheader('Solusi Bisnis')
assesing_data(payments_df, customers_df)
cleaning_data(orders_df)
st.write('untuk menjawab pertanyaan bisnis, sebelumnya saya melakukan beberapa langkah pada background yakni Assessing Data dan Cleaning Data. Selanjutnya saya melakukan pengolahan data dari olist_order_payments_dataset.csv dan olist_customers_dataset.csv dengan menyatukan data olist_orders_dataset.csv bedasarkan order_id, diperoleh data sebagai berikut')

col1, col2= st.columns(2)
with col1:
    st.write("<div style='text-align:center'><b>Data Payments & Orders:</b></div>", unsafe_allow_html=True)
    st.write(merge_data_payment_order(payments_df, orders_df))
with col2:
    st.write("<div style='text-align:center'><b>Data Customers & Orders:</b></div>", unsafe_allow_html=True)
    st.write(merge_data_customer_order(customers_df, orders_df))


st.subheader('Solusi Bisnis 1 :')
st.write('1.  Metode pembayaran manakah yang paling umum digunakan pelanggan Olist Departement Store ?')
st.write('untuk menjawab pertanyaan pertama saya melakukan pengolahan data yang didapat dari penggabungan olist_order_payments_dataset.csv dengan olist_orders_dataset.csv berdasarkan order_id yang disimpan ke dalam main_data_payment_order.csv untuk dilakukan analisa data sehingga dapat menghasilkan visual Metode pembayaran populer berdasarkan data banyaknya yang menggunakan metode pembayaran tertentu sebagai berikut')
create_plot_payment_popular()

st.subheader('Solusi Bisnis 2 :')
st.write('2.  Darimanakah kota asal dengan populasi terbesar pelanggan Olist Departement Store ? ')
st.write('untuk menjawab pertanyaan kedua saya melakukan pengolahan data yang didapat dari penggabungan olist_customers_dataset.csv dengan olist_orders_dataset.csv berdasarkan order_id yang disimpan ke dalam main_data_customer_order.csv untuk dilakukan analisa data sehingga dapat menghasilkan visual Kota asal pelanggan berdasarkan data banyaknya pelanggan dari kota tertentu sebagai berikut')
create_plot_cities_popular()

st.subheader('Conclusion')
st.write('1. Jenis Pembayaran yang Paling Banyak Digunakan: Data menunjukkan bahwa metode pembayaran yang paling banyak digunakan adalah kartu kredit (credit card) dengan total transaksi sebanyak 76.505 kali.')
st.write('2. Kota dengan Populasi Customer Terbesar: Berdasarkan data, kota Sao Paulo memiliki populasi pelanggan terbesar dengan total 15.540 pelanggan.')
st.success('Dengan demikian, dari hasil analisis ini, kita dapat menarik kesimpulan bahwa Sao Paulo memiliki jumlah pelanggan yang signifikan dan mayoritas pelanggan menggunakan kartu kredit sebagai metode pembayaran utama. Informasi ini dapat memberikan wawasan yang berharga bagi pengambil keputusan dalam merencanakan strategi pemasaran dan layanan pelanggan di wilayah Sao Paulo dan Metode Pembayaran Kartu Kredit.')
