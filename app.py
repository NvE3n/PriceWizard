import streamlit as st
import pickle

st.title('Laptop Price Estimator')

with st.form("my_form"):
    Company_list = ['Acer', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Other']
    Typename_list = ['Notebook', 'Gaming', 'Ultrabook', 'Convertible', 'Workstation', 'Netbook']
    Inches_list = [10.1, 11.3, 11.6, 12.0, 12.3, 12.5, 13.0, 13.3, 13.5, 13.9, 14.0, 14.1, 15.0, 15.4, 15.6, 17.0, 17.3, 18.4]
    OpSys_list = ['Windows 10', 'No OS', 'Linux', 'Windows 7', 'Chrome OS', 'macOS', 'Mac OS X', 'Windows 10 S', 'Android']
    Resolution_list = ['1920x1080', '1366x768', '3840x2160', '3200x1800', '2560x1440', '1600x900', '2560x1600', '2304x1440', '2256x1504', '1920x1200', '1440x900', '2880x1800', '2400x1600', '2160x1440', '2736x1824']
    CpuBrand_list = ['Intel', 'AMD']
    GpuBrand_list = ['Intel HD', 'Nvidia GeForce', 'AMD Radeon', 'Intel UHD', 'Nvidia Quadro', 'Intel Iris', 'Other']

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
    input_array = [float(Inches), int(Ram), float(Weight), (1 if FullHD == True else 0), (1 if IpsPanel == True else 0), (1 if UltraHD == True else 0),
                   (1 if TouchScreen == True else 0), (1 if QuadHD == True else 0), (1 if RetinaDisplay == True else 0), float(CpuGHz), (1 if Company == 'Acer' else 0),
                   (1 if Company == 'Asus' else 0), (1 if Company == 'Dell' else 0), (1 if Company == 'HP' else 0), (1 if Company == 'Lenovo' else 0),
                   (1 if Company == 'MSI' else 0), (1 if Company == 'Other' else 0), (1 if TypeName == 'Convertible' else 0),
                   (1 if TypeName == 'Gaming' else 0), (1 if TypeName == 'Netbook' else 0), (1 if TypeName == 'Notebook' else 0),
                   (1 if TypeName == 'Ultrabook' else 0), (1 if TypeName == 'Workstation' else 0), (1 if OpSys == 'Android' else 0),
                   (1 if OpSys == 'Chrome OS' else 0),  (1 if OpSys == 'Linux' else 0),  (1 if OpSys == 'Mac OS X' else 0), (1 if OpSys == 'No OS' else 0), 
                   (1 if OpSys == 'Windows 10' else 0), (1 if OpSys == 'Windows 10 S' else 0), (1 if OpSys == 'Windows 7' else 0),
                   (1 if OpSys == 'macOS' else 0), (1 if Resolution == '1366x768' else 0), (1 if Resolution == '1440x900' else 0),
                   (1 if Resolution == '1600x900' else 0), (1 if Resolution == '1920x1080' else 0), (1 if Resolution == '1920x1200' else 0),
                   (1 if Resolution == '2160x1440' else 0), (1 if Resolution == '2256x1504' else 0), (1 if Resolution == '2304x1440' else 0),
                   (1 if Resolution == '2400x1600' else 0), (1 if Resolution == '2560x1440' else 0), (1 if Resolution == '2560x1600' else 0),
                   (1 if Resolution == '2736x1824' else 0), (1 if Resolution == '2880x1800' else 0), (1 if Resolution == '3200x1800' else 0),
                   (1 if Resolution == '3200x1800' else 0), (1 if CpuBrand == 'AMD' else 0), (1 if CpuBrand == 'Intel' else 0),
                   (1 if GpuBrand == 'AMD Radeon' else 0), (1 if GpuBrand == 'Intel HD' else 0), (1 if GpuBrand == 'Intel Iris' else 0),
                   (1 if GpuBrand == 'Intel UHD' else 0), (1 if GpuBrand == 'Nvidia GeForce' else 0),
                   (1 if GpuBrand == 'Nvidia Quadro' else 0), (1 if GpuBrand == 'Other' else 0)]


    # Display prediction
    st.header(f"Predicted Price: LKR.")
