import streamlit as st
from API_call import note_generator , audio_transcription , quiz_generator
from PIL import Image

st.title("Notes Summary And Quiz Generator" , anchor=False)
st.markdown("Upload Up to Three Images to Generate a Notes Summary and Quiz")
st.divider()

with st.sidebar:
    st.header("Controls")
    # Working with images
    images = st.file_uploader(
        "Upload The Photos of Your Notes",
        type=["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"],
        accept_multiple_files=True
    )

    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)
    
    if images:
        if len(images) > 3:
            st.error("Please upload a maximum of three images only.")

        else:
            st.subheader("Uploaded Images")
            col = st.columns(len(images))
            for i , img in enumerate(images):
                with col[i]:
                    st.image(img)

    st.markdown("")
    st.markdown("")

    # Working with difficulty
    difficulty = st.selectbox(
        "Enter The Difficulty Level of your Quiz",
        ("Easy" , "Medium" , "Hard"),
        index=None
        )
    pressed = st.button("Click The Button To initiate AI" , type="primary")

if pressed:
    if not images:
        st.error("Please upload at least one image.")
    if not difficulty:
        st.error("Please select a difficulty level.")

    if images and difficulty:
        #Note container
        with st.container(border=True):
            with st.spinner("AI is writing for you..."):
                st.subheader("Your Note :",anchor = False)
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)

        #Audio Container
        with st.container(border=True):
            with st.spinner("AI is making for you..."):
                st.subheader("Audio Transcription :",anchor = False)

                generated_notes = generated_notes.replace("#" , "")
                generated_notes = generated_notes.replace("*" , "")
                generated_notes = generated_notes.replace("-" , "")
                generated_notes = generated_notes.replace("_" , "")

                st.audio(audio_transcription(generated_notes))

        # Quiz Container
        with st.container(border=True):
            with st.spinner("AI is writing for you..."):
                st.subheader(f"Quizz ({difficulty}):",anchor = False)
                quizzes = quiz_generator(pil_images , difficulty)
                st.text(quizzes)

        #correct ans part
        # with st.container(border=True):
        #     st.subheader("Correct Answers (Please press 1 time):", anchor=False)
        #     if st.button("Show Answers"):
        #         with st.spinner("Fetching answers..."):
        #             ans = correct_ans(quizzes)
        #             st.markdown(ans)
