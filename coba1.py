import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk simulasi perubahan kecepatan motor
def motor_speed_simulation():
    # Parameter
    t = np.linspace(0, 10, 1000)  # waktu dari 0 s hingga 10 s, dengan 1000 titik data
    speed = np.zeros_like(t)  # array untuk kecepatan, mulai dari 0 km/jam
    max_speed = 60  # kecepatan maksimal saat pedal gas penuh (60 km/jam)

    # Simulasi perubahan kecepatan
    for i, time in enumerate(t):
        if time < 2:
            speed[i] = 0  # sebelum t = 2 detik, kecepatan tetap 0
        elif 2 <= time <= 6:
            # Pedal gas penuh dari t = 2 hingga t = 6, kecepatan bertambah secara linier
            speed[i] = max_speed * ((time - 2) / (6 - 2))
        elif 6 < time <= 7:
            # Kecepatan mencapai maksimal 60 km/jam
            speed[i] = max_speed
        else:
            # Pedal gas diturunkan ke 0% setelah t = 7 detik, kecepatan menurun
            speed[i] = max_speed * ((10 - time) / (10 - 7))

    # Plot perubahan kecepatan
    plt.figure(figsize=(10, 6))
    plt.plot(t, speed, label="Kecepatan Motor", color="blue")
    plt.xlabel("Waktu (detik)")
    plt.ylabel("Kecepatan (km/jam)")
    plt.title("Simulasi Perubahan Kecepatan Motor")
    plt.legend()
    plt.grid(True)
    plt.show()

# Jalankan simulasi
motor_speed_simulation()
