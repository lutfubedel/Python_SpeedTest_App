import customtkinter as ctk
import speedtest
from tkinter import messagebox
import threading

# İnternet hızını ölçen fonksiyon (loading göstergesi ile)
def internet_hizini_olc():
    # Arka planda çalışması için threading kullanıyoruz
    def hiz_testi():
        try:
            # Dönen yuvarlağı göster
            spinner_label.pack(pady=20)  # Spinner'ı ortala ve göster
            spinner_label.start()
            
            st = speedtest.Speedtest()
            st.get_best_server()

            # İndirme ve yükleme hızlarını ölç
            indirme_hizi = st.download() / 10**6  # Mbps cinsine dönüştür
            yukleme_hizi = st.upload() / 10**6  # Mbps cinsine dönüştür

            # Sonuçları etiketlere yerleştir
            indirme_label.configure(text=f"İndirme Hızı: {indirme_hizi:.2f} Mbps")
            yukleme_label.configure(text=f"Yükleme Hızı: {yukleme_hizi:.2f} Mbps")
        
        except Exception as e:
            messagebox.showerror("Hata", f"Hız testi gerçekleştirilemedi: {str(e)}")
        
        finally:
            # Dönen yuvarlağı gizle
            spinner_label.stop()
            spinner_label.pack_forget()

    # Threading ile arka planda test çalıştırma
    test_thread = threading.Thread(target=hiz_testi)
    test_thread.start()

# CustomTkinter tema ayarları
ctk.set_appearance_mode("dark")  # 'dark' veya 'light'
ctk.set_default_color_theme("blue")  # 'blue', 'green', 'dark-blue'

# Ana pencere ayarları
window = ctk.CTk()
window.title("İnternet Hız Testi")
window.geometry("400x400")

# Başlık
label = ctk.CTkLabel(window, text="İnternet Hız Testi", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=20)

# İndirme hızı etiketi
indirme_label = ctk.CTkLabel(window, text="İndirme Hızı: - Mbps")
indirme_label.pack(pady=10)

# Yükleme hızı etiketi
yukleme_label = ctk.CTkLabel(window, text="Yükleme Hızı: - Mbps")
yukleme_label.pack(pady=10)

# Hız testi başlat butonu
test_button = ctk.CTkButton(window, text="Hız Testi Başlat", command=internet_hizini_olc)
test_button.pack(pady=20)

# Yükleniyor animasyonu (dönen yuvarlak)
spinner_label = ctk.CTkProgressBar(window, mode='indeterminate')

# Spinner gizli olacak, ölçüm başladığında gösterilecek
spinner_label.pack_forget()

# Pencereyi çalıştır
window.mainloop()
