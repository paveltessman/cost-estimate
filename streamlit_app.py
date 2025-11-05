import streamlit as st

st.set_page_config(page_title="Translation Cost Estimator", layout="wide")

st.title("📚 Educational Materials Translation Cost Estimator")

st.markdown("""
Estimate the cost of translating educational materials including text, images, and videos.
""")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.header("📝 Text Translation")
    
    translation_method = st.radio(
        "Translation Method:",
        ["LLM (Token-based)", "Traditional Service (Character-based)"],
        help="Choose between LLM translation (charged per token) or traditional translation service (charged per character)"
    )
    
    if translation_method == "LLM (Token-based)":
        text_tokens = st.number_input(
            "Number of Text Tokens:",
            min_value=0,
            value=10000,
            step=1000,
            help="Total number of tokens in the text to translate"
        )
        cost_per_token = st.number_input(
            "Cost per Token ($):",
            min_value=0.0,
            value=0.000002,
            format="%.8f",
            help="Cost in dollars per token (e.g., 0.000002 for $2 per million tokens)"
        )
        text_cost = text_tokens * cost_per_token
    else:
        text_characters = st.number_input(
            "Number of Text Characters:",
            min_value=0,
            value=50000,
            step=5000,
            help="Total number of characters in the text to translate"
        )
        cost_per_character = st.number_input(
            "Cost per Character ($):",
            min_value=0.0,
            value=0.00001,
            format="%.8f",
            help="Cost in dollars per character"
        )
        text_cost = text_characters * cost_per_character

with col2:
    st.header("🖼️ Images")
    
    num_images = st.number_input(
        "Number of Images:",
        min_value=0,
        value=50,
        step=10,
        help="Total number of images to process"
    )
    
    cost_per_image = st.number_input(
        "Cost per Image ($):",
        min_value=0.0,
        value=0.05,
        format="%.4f",
        help="Cost in dollars per image"
    )
    
    image_cost = num_images * cost_per_image
    
    st.header("🎥 Videos")
    
    video_seconds = st.number_input(
        "Total Video Duration (seconds):",
        min_value=0,
        value=600,
        step=60,
        help="Total duration of all videos in seconds"
    )
    
    cost_per_second = st.number_input(
        "Cost per Second ($):",
        min_value=0.0,
        value=0.10,
        format="%.4f",
        help="Cost in dollars per second of video"
    )
    
    video_cost = video_seconds * cost_per_second

# Calculate total cost
st.divider()

st.header("💰 Cost Breakdown")

col_a, col_b, col_c, col_d = st.columns(4)

with col_a:
    st.metric("Text Translation", f"${text_cost:.2f}")
    if translation_method == "LLM (Token-based)":
        st.caption(f"{text_tokens:,} tokens")
    else:
        st.caption(f"{text_characters:,} characters")

with col_b:
    st.metric("Images", f"${image_cost:.2f}")
    st.caption(f"{num_images} images")

with col_c:
    st.metric("Videos", f"${video_cost:.2f}")
    st.caption(f"{video_seconds} seconds ({video_seconds//60} min {video_seconds%60} sec)")

with col_d:
    total_cost = text_cost + image_cost + video_cost
    st.metric("TOTAL COST", f"${total_cost:.2f}", delta=None)

st.divider()

# Detailed breakdown
with st.expander("📊 Detailed Breakdown"):
    st.markdown(f"""
    **Text Translation ({translation_method}):**
    - {'Tokens' if translation_method == 'LLM (Token-based)' else 'Characters'}: {text_tokens if translation_method == 'LLM (Token-based)' else text_characters:,}
    - Cost per {'token' if translation_method == 'LLM (Token-based)' else 'character'}: ${cost_per_token if translation_method == 'LLM (Token-based)' else cost_per_character:.8f}
    - Subtotal: ${text_cost:.2f}
    
    **Images:**
    - Number of images: {num_images}
    - Cost per image: ${cost_per_image:.4f}
    - Subtotal: ${image_cost:.2f}
    
    **Videos:**
    - Duration: {video_seconds} seconds ({video_seconds/60:.1f} minutes)
    - Cost per second: ${cost_per_second:.4f}
    - Subtotal: ${video_cost:.2f}
    
    **Total Estimated Cost: ${total_cost:.2f}**
    """)

st.divider()
st.caption("💡 Tip: Adjust the values above to see how different quantities and pricing affect your total cost.")
