import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data():

    payments_df = pd.read_csv('data/olist_order_payments_dataset.csv', delimiter=',')

    customers_df = pd.read_csv('data/olist_customers_dataset.csv', delimiter=',')

    orders_df = pd.read_csv('data/olist_orders_dataset.csv', delimiter=',')

    return payments_df, customers_df, orders_df

def assesing_data(payments_df, customers_df):
    # cek tipe data, terdapat perbedaan jumlah data, cek missing value pada table customers_df
    # cek missing value pada table customers_df
    customers_df.isna().sum()
    # cek missing duplikasi pada table customers_df
    customers_df.duplicated().sum()

    # cek tipe data, terdapat perbedaan jumlah data, cek missing value pada table payments_df
    # cek missing value pada table payments_df
    payments_df.isna().sum()
    # cek missing duplikasi pada table payments_df
    payments_df.duplicated().sum()

def cleaning_data(orders_df):
    # drop duplikasi pada table order
    orders_df.drop_duplicates(inplace=True)

def merge_data_payment_order(payments_df, orders_df):
    payments_order_df = pd.merge(
        left=payments_df,
        right=orders_df,
        how="left",
        left_on="order_id",
        right_on="order_id"
    )
    payments_order_df.to_csv("main_data_payment_order.csv", index=False)
    return payments_order_df

def merge_data_customer_order(customers_df, orders_df):
    customer_order_df = pd.merge(
        left=customers_df,
        right=orders_df,
        how="left",
        left_on="customer_id",
        right_on="customer_id"
    )
    customer_order_df.to_csv("main_data_customer_order.csv", index=False)
    return customer_order_df

def create_plot_payment_popular():
    payments_order_df = pd.read_csv('dashboard/main_data_payment_order.csv', delimiter=',')
    # Mengelompokkan data dan menghitung jumlah order unik untuk setiap jenis pembayaran
    payment_counts = payments_order_df.groupby(by="payment_type").order_id.nunique().sort_values(ascending=False).reset_index().head(10)

    # Mengganti nama kolom
    payment_counts = payment_counts.rename(columns={"payment_type": "Metode Pembayaran", "order_id": "Jumlah Pembayaran"})

    st.write("<div style='text-align:center'><b>Data Metode Pembayaran :</b></div>", unsafe_allow_html=True)
    col1, col2= st.columns(2)
    with col1:
        # Menampilkan data rekapitulasi
        st.write(payment_counts)
    with col2:
        # Membuat plot
        plt.barh(y=payment_counts['Metode Pembayaran'], width=payment_counts['Jumlah Pembayaran'])

        # Menambahkan label pada sumbu x dan y
        plt.xlabel('Jumlah Order')
        plt.ylabel('Metode Pembayaran')

        # Menambahkan judul plot
        plt.title('Grafik Jumlah Pembayaran Berdasarkan Jenis')

        # You can disable this warning by disabling the config option: deprecation.showPyplotGlobalUse  
        st.set_option('deprecation.showPyplotGlobalUse', False)

        # Menampilkan plot
        st.pyplot()


def create_plot_cities_popular():
    customer_order_df = pd.read_csv('dashboard/main_data_customer_order.csv', delimiter=',')
    # Mengelompokkan data dan menghitung jumlah order unik untuk setiap jenis pembayaran
    cities_counts = customer_order_df.groupby(by="customer_city").order_id.nunique().sort_values(ascending=False).reset_index().head(10)

    # Mengganti nama kolom
    cities_counts = cities_counts.rename(columns={"customer_city": "Asal Kota", "order_id": "Jumlah Pelanggan"})

    st.write("<div style='text-align:center'><b>Data Kota Asal Pelanggan :</b></div>", unsafe_allow_html=True)
    col1, col2= st.columns(2)
    with col1:
        # Menampilkan data rekapitulasi
        st.write(cities_counts)
    with col2:
        # Membuat plot
        plt.barh(y=cities_counts['Asal Kota'], width=cities_counts['Jumlah Pelanggan'])

        # Menambahkan label pada sumbu x dan y
        plt.xlabel('Jumlah Pelanggan')
        plt.ylabel('Asal Kota Pelanggan')

        # Menambahkan judul plot
        plt.title('Grafik Jumlah Asal Kota Pelanggan Berdasarkan Kota')

        # You can disable this warning by disabling the config option: deprecation.showPyplotGlobalUse  
        st.set_option('deprecation.showPyplotGlobalUse', False)

        # Menampilkan plot
        st.pyplot()
