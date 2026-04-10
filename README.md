# 📱 Mobile Price Prediction App

Ứng dụng dự đoán giá điện thoại thông minh dựa trên các thông số kỹ thuật phần cứng. Dự án sử dụng mô hình học máy để tìm ra mối liên hệ giữa cấu hình và giá thành sản phẩm.

## 🚀 Tính năng chính
- **Dự đoán giá (Prediction):** Nhập cấu hình tùy chỉnh để nhận mức giá dự kiến.
- **Dữ liệu thực tế:** Các thanh trượt lựa chọn thông số được trích xuất trực tiếp từ tập dữ liệu mẫu.
- **Phân tích tương quan:** Sử dụng các thư viện đồ họa để trực quan hóa tầm quan trọng của các biến.

## 🛠 Công nghệ và Thư viện sử dụng
Dự án được xây dựng dựa trên các công nghệ hàng đầu về khoa học dữ liệu:
- **Ngôn ngữ:** Python
- **Xử lý dữ liệu:** `pandas`, `numpy`
- **Học máy (ML):** `scikit-learn` (Linear Regression, StandardScaler, train_test_split)
- **Trực quan hóa:** `matplotlib`, `seaborn`
- **Giao diện Web:** `streamlit`

## 📊 Quy trình thực hiện (Workflow)
1. **Tiền xử lý:** Làm sạch dữ liệu và chuẩn hóa thông số bằng `StandardScaler`.
2. **Phân tích (EDA):** Sử dụng Heatmap để xem mối tương quan giữa Pin, RAM, CPU... với Giá tiền.
3. **Huấn luyện:** Chia tập dữ liệu (train/test) và huấn luyện mô hình Hồi quy tuyến tính.
4. **Đánh giá:** Đo lường sai số bằng các chỉ số `MSE` (Mean Squared Error) và `MAE` (Mean Absolute Error).

## 📂 Cấu trúc thư mục
```text
MOBILE_PRICE_PREDICTION/
├── data/
│   └── Cellphone.csv      # Tập dữ liệu gốc
├── app.py                 # File chạy giao diện chính
├── main.ipynb             # File nghiên cứu và phân tích
├── requirements.txt       # Danh sách thư viện cài đặt
└── README.md              # Hướng dẫn dự án
```

---

## 💻 Hướng dẫn cài đặt và chạy
1. **Clone dự án:**
   ```bash
   git clone [https://github.com/TranGiaHy/mobile-price-prediction.git](https://github.com/TranGiaHy/mobile-price-prediction.git)
   cd mobile-price-prediction
   ```

2. **Cài đặt thư viện:**
   ```bash
   pip install -r requirements.txt
   ``` 

3. **Chạy ứng dụng:**
   ```bash
   streamlit run app.py
   ```

---

## 📝 Tác giả
TranGiaHy - [https://github.com/TranGiaHy](https://github.com/TranGiaHy)

📝 Đánh giá mô hình
Mô hình hiện tại đạt các chỉ số sai số thấp trên tập kiểm tra, cho phép dự đoán khá chính xác các dòng điện thoại tầm trung và cao cấp.

Tác giả: TranGiaHy
Link github: [https://github.com/TranGiaHy](https://github.com/TranGiaHy)
---

### 💡 Lưu ý quan trọng cho file `requirements.txt`:

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
```
  