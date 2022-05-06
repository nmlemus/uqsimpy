from PIL import Image

image = Image.open('/home/nmlemus/research/uqsimpy/assets/logo2.png')


def set_sidebar(st):
    st.sidebar.image(image, width=180)
    st.sidebar.title('UQSim')

    objective = st.sidebar.radio('',
                                 ('Create Model', 'Simulate', 'Uncertainty Quantification', 'Parameter Estimation',
                                  'Sensitivity Analysis', 'Info'))

    return objective
