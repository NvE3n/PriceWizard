import streamlit as st
import pickle

st.title('Laptop Price Estimator')

with st.form("my_form"):
    Company_list = ['Acer', 'Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Toshiba', 'Other']
    Typename_list = ['Notebook', 'Gaming', 'Ultrabook', 'Convertible', 'Workstation', 'Netbook']
    Inches_list = [10.1, 11.3, 11.6, 12.0, 12.3, 12.5, 13.0, 13.3, 13.5, 13.9, 14.0, 14.1, 15.0, 15.4, 15.6, 17.0, 17.3, 18.4]
    OpSys_list = ['Windows 10', 'No OS', 'Linux', 'Windows 7', 'Other']
    Resolution_list = ['1920x1080', '1366x768', '3840x2160', '3200x1800', '2560x1440', '1600x900', '2560x1600', '2304x1440', '2256x1504', '1920x1200', '1440x900', '2880x1800', '2400x1600', '2160x1440', '2736x1824']
    CpuBrand_list = ['Intel', 'AMD', 'Samsung']
    GpuBrand_list = ['AMD FirePro', 'AMD R17M-M1-70', 'AMD R4', 'AMD Radeon', 'ARM Mali', 'Intel Graphics', 'Intel HD', 'Intel Iris', 'Intel UHD', 'Nvidia GTX', 'Nvidia GeForce', 'Nvidia Quadro']

    # User input widgets
    Company = st.selectbox('Select company', Company_list)
    TypeName = st.selectbox('Select type', Typename_list)
    Inches = st.selectbox('Select inches of laptop', Inches_list)
    Ram = st.number_input('Select RAM (GB)', min_value=1, max_value=64, step=1)
    OpSys = st.selectbox('Select operating system', OpSys_list)
    Weight = st.number_input('Select laptop weight (kg)', min_value=0.69, max_value=4.70, step=0.1, format="%.2f")
    Resolution = st.selectbox('Select resolution type', Resolution_list)

    col1, col2, col3 = st.columns(3)

    with col1:
        FullHD = st.checkbox("Full HD")
        TouchScreen = st.checkbox("Touch Screen")

    with col2:
        IpsPanel = st.checkbox("IPS Panel")
        QuadHD = st.checkbox("Quad HD")

    with col3:
        UltraHD = st.checkbox("Ultra HD")
        RetinaDisplay = st.checkbox("Retina Display")

    CpuBrand = st.selectbox('Select CPU brand', CpuBrand_list)
    CpuGHz = st.number_input('Select CPU frequency (GHz)', min_value=0.90, max_value=3.60, step=0.1, format="%.2f")
    GpuBrand = st.selectbox('Select GPU brand', GpuBrand_list)

    submitted = st.form_submit_button("Submit")

# Process form submission outside the form context
if submitted:
    input_array = [float(Inches), float(Ram), float(Weight), (1 if FullHD else 0), (1 if IpsPanel else 0),
                   (1 if UltraHD else 0), (1 if TouchScreen else 0), (1 if QuadHD else 0), (1 if RetinaDisplay else 0), float(CpuGHz),
                   (True if Company == 'Acer' else False), (True if Company == 'Apple' else False), (True if Company == 'Asus' else False), (True if Company == 'Dell' else False),
                   (True if Company == 'HP' else False), (True if Company == 'Lenovo' else False), (True if Company == 'MSI' else False), (True if Company == 'Other' else False),
                   (True if Company == 'Toshiba' else False), (True if TypeName == 'Convertible' else False), (True if TypeName == 'Gaming' else False),
                   (True if TypeName == 'Netbook' else False), (True if TypeName == 'Notebook' else False), (True if TypeName == 'Ultrabook' else False),
                   (True if TypeName == 'Workstation' else False), (True if OpSys == 'Linux' else False), (True if OpSys == 'No OS' else False), (True if OpSys == 'Other' else False),
                   (True if OpSys == 'Windows 10' else False), (True if OpSys == 'Windows 7' else False), (True if Resolution == '1366x768' else False),
                   (True if Resolution == '1440x900' else False), (True if Resolution == '1600x900' else False), (True if Resolution == '1920x1080' else False),
                   (True if Resolution == '1920x1200' else False), (True if Resolution == '2560x1440' else False), (True if Resolution == '2256x1504' else False),
                   (True if Resolution == '2304x1440' else False), (True if Resolution == '2400x1600' else False), (True if Resolution == '2160x1440' else False),
                   (True if Resolution == '2560x1600' else False), (True if Resolution == '2736x1824' else False), (True if Resolution == '2880x1800' else False),
                   (True if Resolution == '3200x1800' else False), (True if Resolution == '3840x2160' else False), (True if CpuBrand == 'AMD' else False),
                   (True if CpuBrand == 'Intel' else False), (True if CpuBrand == 'Samsung' else False), (True if GpuBrand == 'AMD FirePro' else False),
                   (True if GpuBrand == 'AMD R17M-M1-70' else False), (True if GpuBrand == 'AMD R4' else False), (True if GpuBrand == 'AMD Radeon' else False),
                   (True if GpuBrand == 'ARM Mali' else False), (True if GpuBrand == 'Intel Graphics' else False), (True if GpuBrand == 'Intel HD' else False),
                   (True if GpuBrand == 'Intel Iris' else False), (True if GpuBrand == 'Intel UHD' else False), (True if GpuBrand == 'Nvidia GTX' else False),
                   (True if GpuBrand == 'Nvidia GeForce' else False), (True if GpuBrand == 'Nvidia Quadro' else False)]

    with open('predictor.pickle', 'rb') as f:
        model = pickle.load(f)

    predicted_price = model.predict([input_array])

    # Display prediction
    st.header(f"Predicted Price: LKR. {(predicted_price[0]*300):.2f}")


