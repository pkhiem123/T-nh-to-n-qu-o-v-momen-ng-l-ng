import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def main():

    t = sp.symbols('t')
    
    print("--- CHƯƠNG TRÌNH TÍNH TOÁN QUỸ ĐẠO VÀ MOMEN ĐỘNG LƯỢNG ---")
    
    x_str = input("Nhập biểu thức cho x(t) (ví dụ: 5*cos(t)): ")
    y_str = input("Nhập biểu thức cho y(t) (ví dụ: 5*sin(t)): ")
    
    try:
        m_val = float(input("Nhập khối lượng m (ví dụ: 2): "))
    except ValueError:
        print("Khối lượng không hợp lệ. Sử dụng giá trị m = 1")
        m_val=1

    try:
        x_expr = sp.sympify(x_str)
        y_expr = sp.sympify(y_str)
    except sp.SympifyError:
        print("Biểu thức nhập vào không hợp lệ.")
        return
    
    print("--- 2. TÍNH TOÁN SYMBOLIC ---")

    vx_expr = sp.diff(x_expr, t)
    vy_expr = sp.diff(y_expr, t)
    v_expr = sp.sqrt(vx_expr**2 + vy_expr**2)
    t_calc=float(input("Nhập thời gian cần tính:"))
    val_v=v_expr.subs(t,t_calc)
    L_expr =(m_val*(x_expr * vy_expr - y_expr * vx_expr))
    L_expr_simplified = sp.simplify(L_expr)
    val_L=L_expr_simplified.subs(t,t_calc)
    print("Kết quả vận tốc ",val_v)
    print("Moment động lượng: ",val_L)
    
    print("--- 3. CHUẨN BỊ VẼ ĐỒ THỊ ---")
    try:
        t_start = float(input("Nhập thời gian bắt đầu t (ví dụ: 0): "))
        t_end = float(input(f"Nhập thời gian kết thúc t (ví dụ: 10): "))
        num_points = int(input("Nhập số điểm tính toán (ví dụ: 500): "))
    except ValueError:
        print("Giá trị không hợp lệ. Sử dụng giá trị mặc định.")
        t_start, t_end, num_points = 0, 10, 500

    t_values = np.linspace(t_start, t_end, num_points)

    func_x = sp.lambdify(t, x_expr, 'numpy')
    func_y = sp.lambdify(t, y_expr, 'numpy')
    func_L = sp.lambdify(t, L_expr_simplified, 'numpy')

    x_values = func_x(t_values)
    y_values = func_y(t_values)
    L_values = func_L(t_values)

    print("Đang hiển thị đồ thị...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Đồ thị 1: Quỹ đạo (y theo x)
    ax1.plot(x_values, y_values, color='blue')
    ax1.set_title(f"1. Đồ thị Quỹ đạo (y theo x)", fontsize=14)
    ax1.set_xlabel("x", fontsize=12)
    ax1.set_ylabel("y", fontsize=12)
    ax1.grid(True)
    ax1.set_aspect('equal', 'box') 

    # Đồ thị 2: Momen động lượng (L theo t)
    ax2.plot(t_values, L_values, color='red')
    ax2.set_title(f"2. Momen động lượng (L theo t)", fontsize=14)
    ax2.set_xlabel("Thời gian t", fontsize=12)
    ax2.set_ylabel("Momen động lượng L", fontsize=12)
    ax2.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()