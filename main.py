import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# JSON dosyasını okuma
with open('portfolio.json', 'r') as file:
    data = json.load(file)

# Verileri çekme
labels = [item["hisse_adi"] for item in data]
sizes_tutari = [item["hisse_tutari"] for item in data]
sizes_adedi = [item["hisse_adedi"] for item in data]

# Pie chart oluşturma
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Hisse tutarı pie chart
axs[0].pie(sizes_tutari, labels=labels, autopct='%1.1f%%', startangle=90)
axs[0].axis('equal')  # Yatay ve dikey ölçeklerin eşitlenmesi
axs[0].set_title('Hisse Tutarı Dağılımı')

# Hisse adedi pie chart
axs[1].pie(sizes_adedi, labels=labels, autopct='%1.1f%%', startangle=90)
axs[1].axis('equal')
axs[1].set_title('Hisse Adedi Dağılımı')

# PDF dosyasına kaydetme
with PdfPages('portfolio_analysis.pdf') as pdf:
    pdf.savefig(fig)

plt.show()