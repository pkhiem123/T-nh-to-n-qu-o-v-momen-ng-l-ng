import sympy as sp #nhập thư viện Sympy vào chương trình (Sympy thư viện cho phép tính toán theo ẩn)
import numpy as np #nhập thư viện Numpy vào chương trình (Numpy thư viện cho phép tính toán nhanh các giá trị)
import matplotlib.pyplot as plt #nhập thư viện matplot để vẽ đồ thị

def main():

    t = sp.symbols('t') #nhập ẩn t (không có dòng này nhập biểu thức vào sẽ bị lỗi)
    
    print("--- CHƯƠNG TRÌNH TÍNH TOÁN QUỸ ĐẠO VÀ MOMEN ĐỘNG LƯỢNG ---")
    
    x_str = input("Nhập biểu thức cho x(t) (ví dụ: 5*cos(t)): ") #người dùng nhập vào biểu thức x theo ẩn t
    y_str = input("Nhập biểu thức cho y(t) (ví dụ: 5*sin(t)): ") #người dùng nhập vào biểu thức y theo ẩn t
    
    try:
        m_val = float(input("Nhập khối lượng m (ví dụ: 2): ")) #người dùng nhập giá trị m (m là số thực)
    except ValueError:
        print("Khối lượng không hợp lệ. Sử dụng giá trị m = 1") #nếu giá trị không hợp lệ sẽ dùng giá trị m=1
        m_val=1

    try:
        x_expr = sp.sympify(x_str) #chuyển biểu thức nhập vào thành dạng Sympy
        y_expr = sp.sympify(y_str)
    except sp.SympifyError:
        print("Biểu thức nhập vào không hợp lệ.") #nếu biểu thức nhập vào không hợp lệ chương trình bắt đầu lại
        return
    
    print("--- 2. TÍNH TOÁN SYMBOLIC ---")

    vx_expr = sp.diff(x_expr, t)#đạo hàm biểu thức x,y theo t
    vy_expr = sp.diff(y_expr, t)
    v_expr = sp.sqrt(vx_expr**2 + vy_expr**2)# tính v theo vx và xy có chứa ẩn t (sqrt là căn bậc hai)
    t_calc=float(input("Nhập thời gian cần tính:")) # nhập vào thời điểm cần tính giá trị v và L.
    val_v=v_expr.subs(t,t_calc) #thay giá trị cần tính vào t để tính v.
    L_expr =(m_val*(x_expr * vy_expr - y_expr * vx_expr)) #tính biểu thức L theo t
    L_expr_simplified = sp.simplify(L_expr) #rút gọn biểu thức L theo t
    val_L=L_expr_simplified.subs(t,t_calc) #thay giá trị cần tính vào t để tính L
    print("Kết quả vận tốc ",val_v) #xuất kết quả
    print("Moment động lượng: ",val_L)
    
    print("--- 3. CHUẨN BỊ VẼ ĐỒ THỊ ---")
    try:
        t_start = float(input("Nhập thời gian bắt đầu t (ví dụ: 0): ")) #nhập các giá trị t để vẽ đồ thị
        t_end = float(input(f"Nhập thời gian kết thúc t (ví dụ: 10): "))
        num_points = int(input("Nhập số điểm tính toán (ví dụ: 500): "))
    except ValueError:
        print("Giá trị không hợp lệ. Sử dụng giá trị mặc định.") #nếu giá trị bị lỗi thì dùng giá trị mặc định.
        t_start, t_end, num_points = 0, 10, 500

    t_values = np.linspace(t_start, t_end, num_points) #tạo các giá trị để tính (giống nhập x trong table ở casio)

    func_x = sp.lambdify(t, x_expr, 'numpy') #chuyển biểu thức sympy thành numpy để tính nhanh các giá trị
    func_y = sp.lambdify(t, y_expr, 'numpy')
    func_L = sp.lambdify(t, L_expr_simplified, 'numpy')

    x_values = func_x(t_values)#tính toán các giá trị giống table trong casio
    y_values = func_y(t_values)
    L_values = func_L(t_values)

    print("Đang hiển thị đồ thị...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7)) #tạo khung, ô để vẽ đồ thị

    # Đồ thị 1: Quỹ đạo (y theo x)
    ax1.plot(x_values, y_values, color='blue') #vẽ y theo x
    ax1.set_title(f"1. Đồ thị Quỹ đạo (y theo x)", fontsize=14) #viết tiêu đề đồ thị
    ax1.set_xlabel("x", fontsize=12) #viết trục ox là x
    ax1.set_ylabel("y", fontsize=12) #viết trục Oy là y
    ax1.grid(True)#bật lưới
    ax1.set_aspect('equal', 'box')#chỉnh tỉ lệ bằng nhau Oy, Ox bằng nhau

    # Đồ thị 2: Momen động lượng (L theo t)
    ax2.plot(t_values, L_values, color='red') #như trên
    ax2.set_title(f"2. Momen động lượng (L theo t)", fontsize=14)
    ax2.set_xlabel("Thời gian t", fontsize=12)
    ax2.set_ylabel("Momen động lượng L", fontsize=12)
    ax2.grid(True)
    plt.tight_layout() #tự động căn chỉnh 2 đồ thị cho đẹp
    plt.show() #hiển thị đồ thị ra cho người xem

if __name__ == "__main__":
    main()