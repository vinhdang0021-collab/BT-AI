pip install folium

import folium

# Tọa độ trung tâm (UEH)
center = [10.762622, 106.682231]
m = folium.Map(location=center, zoom_start=15)

# Danh sách địa điểm công cộng
places = [
    {"name": "Bệnh viện Chợ Rẫy", "coords": [10.7546, 106.6636]},
    {"name": "Bến xe Miền Đông", "coords": [10.8010, 106.7100]},
    {"name": "UBND Quận 1", "coords": [10.7769, 106.7009]},
    {"name": "Vincom Center", "coords": [10.7765, 106.7004]},
    {"name": "Ga Sài Gòn", "coords": [10.7820, 106.6770]}
]

# Thêm marker
for place in places:
    folium.Marker(
        location=place["coords"],
        popup=place["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Thêm lớp điều khiển
folium.LayerControl().add_to(m)

# Hiển thị trực tiếp trong Colab
m