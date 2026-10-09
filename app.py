
import streamlit as st

st.set_page_config(
    page_title="AI Marketing Strategy Manager",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Marketing Strategy Manager")
st.markdown(
    "### Turn your business idea into a marketing strategy."
)
st.write(
    "Enter your business details below to generate a "
    "personalized marketing plan."
)

st.divider()

with st.form("marketing_form"):
    st.subheader("🏢 Business Information")

    business_name = st.text_input(
        "Business Name",
        placeholder="e.g. FreshBite"
    )

    product = st.text_input(
        "Product or Service",
        placeholder="e.g. Healthy snacks"
    )

    col1, col2 = st.columns(2)

    with col1:
        audience = st.text_input(
            "Target Audience",
            placeholder="e.g. College students"
        )

    with col2:
        budget = st.selectbox(
            "Monthly Marketing Budget",
            ["Under ₹5,000", "₹5,000–₹15,000",
             "₹15,000–₹50,000", "₹50,000+"]
        )

    goal = st.selectbox(
        "Main Marketing Goal",
        [
            "Increase Brand Awareness",
            "Get More Customers",
            "Increase Sales",
            "Grow Social Media",
            "Launch a New Product"
        ]
    )

    platforms = st.multiselect(
        "Preferred Marketing Platforms",
        ["Instagram", "YouTube", "Facebook",
         "Google", "LinkedIn", "WhatsApp"],
        default=["Instagram"]
    )

    submitted = st.form_submit_button(
        "✨ Generate Marketing Strategy",
        use_container_width=True
    )

if submitted:
    if not business_name.strip() or not product.strip():
        st.warning("Please enter your business name and product.")
    else:
        st.session_state["business_details"] = {
            "business_name": business_name,
            "product": product,
            "audience": audience or "General audience",
            "budget": budget,
            "goal": goal,
            "platforms": platforms
        }

        st.success("Your business details have been received!")

        st.subheader("📋 Your Marketing Strategy")

        st.markdown("#### 1. Business Overview")
        st.write(f"**Business:** {business_name}")
        st.write(f"**Product/Service:** {product}")
        st.write(f"**Target Audience:** {audience or 'General audience'}")

        st.markdown("#### 2. Marketing Goal")
        st.write(goal)

        st.markdown("#### 3. Recommended Platforms")
        if platforms:
            for platform in platforms:
                st.write(f"- {platform}")
        else:
            st.write("Choose suitable platforms based on your audience.")

        st.markdown("#### 4. Suggested Action Plan")
        st.write("**Week 1:** Research your audience and competitors.")
        st.write("**Week 2:** Prepare content and branding materials.")
        st.write("**Week 3:** Publish content and engage with customers.")
        st.write("**Week 4:** Review results and improve your campaign.")

        st.markdown("#### 5. Budget")
        st.write(f"Selected monthly budget: {budget}")

        st.info(
            "This is a starter strategy generated using predefined "
            "templates. Live AI analysis will be added separately."
        )

st.divider()
st.caption("AI Marketing Strategy Manager | Project Demo")
