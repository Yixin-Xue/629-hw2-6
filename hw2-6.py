import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


st.set_page_config(page_title="Logistic Curve Explorer", page_icon="📈")


def logistic_curve(x: np.ndarray, b0: float, b1: float) -> np.ndarray:
    return 1 / (1 + np.exp(-(b0 + b1 * x)))


st.title("Logistic Curve Explorer")
st.write(
    "Adjust the sliders for b0 and b1 to see how they change "
    "the logistic curve f(x) = (1 + exp(-b0 - b1 x))^(-1)."
)

b0 = st.slider("b0", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
b1 = st.slider("b1", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)

x = np.linspace(-10, 10, 500)
y = logistic_curve(x, b0, b1)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color="#1f77b4", linewidth=2, label="Logistic curve")
ax.axhline(0.5, color="gray", linestyle="--", linewidth=1)
ax.axvline(0, color="gray", linestyle="--", linewidth=1)
ax.set_title(f"f(x) with b0 = {b0:.1f}, b1 = {b1:.1f}")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_xlim(-10, 10)
ax.set_ylim(0, 1)
ax.grid(True, alpha=0.3)
ax.legend()

st.pyplot(fig)
