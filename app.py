import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. HUẤN LUYỆN LẠI MÔ HÌNH
df = pd.read_csv('data/cellphone.csv') 

features = ['ram', 'battery', 'internal mem', 'cpu freq', 'ppi', 'RearCam', 'thickness']
X = df[features]
y = df['Price']

model = LinearRegression()
model.fit(X, y)

# 2. XÂY DỰNG GIAO DIỆN WEB
st.title("📱 Ứng dụng Dự đoán Giá Điện thoại")
st.write("Đồ án Học máy: Dự đoán dựa trên cấu hình thực tế từ dữ liệu")

st.sidebar.header("Tùy chỉnh thông số điện thoại:")

# Hàm để lấy danh sách giá trị duy nhất, sắp xếp tăng dần từ CSV
def get_unique_sorted(column_name):
    return sorted(df[column_name].unique())

# Cập nhật các thanh trượt thành select_slider để khớp với dữ liệu CSV
ram_val = st.sidebar.select_slider(
    "Dung lượng RAM (GB)", options=get_unique_sorted('ram')
)

battery_val = st.sidebar.select_slider(
    "Dung lượng Pin (mAh)", options=get_unique_sorted('battery')
)

mem_val = st.sidebar.select_slider(
    "Bộ nhớ trong (GB)", options=get_unique_sorted('internal mem')
)

cpu_val = st.sidebar.select_slider(
    "Tốc độ CPU (GHz)", options=get_unique_sorted('cpu freq')
)

ppi_val = st.sidebar.select_slider(
    "Mật độ điểm ảnh (PPI)", options=get_unique_sorted('ppi')
)

cam_val = st.sidebar.select_slider(
    "Camera sau (MP)", options=get_unique_sorted('RearCam')
)

thick_val = st.sidebar.select_slider(
    "Độ dày (mm)", options=get_unique_sorted('thickness')
)

# Gom dữ liệu đầu vào
input_data = pd.DataFrame({
    'ram': [ram_val], 
    'battery': [battery_val], 
    'internal mem': [mem_val],
    'cpu freq': [cpu_val],
    'ppi': [ppi_val],
    'RearCam': [cam_val],
    'thickness': [thick_val]
})

# 3. DỰ ĐOÁN VÀ HIỂN THỊ
prediction = model.predict(input_data)
gia_tien = prediction[0] # Sửa lỗi cũ bằng cách lấy phần tử đầu tiên

st.info("---")
st.subheader("Cấu hình bạn đã chọn:")
st.write(input_data)

st.success(f"💰 Mức giá dự kiến cho cấu hình này là: **${gia_tien:.2f}**")