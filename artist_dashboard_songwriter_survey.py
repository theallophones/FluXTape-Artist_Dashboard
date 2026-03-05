import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide", page_title="FluXTape Artist Dashboard (Demo)", page_icon="🎚️")

# Custom CSS matching REF 7 aesthetic
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap');

[data-testid="stAppViewContainer"] {
  background: linear-gradient(160deg, #0f1115 0%, #1a1d25 100%) fixed !important;
}
[data-testid="stHeader"] {
  background: rgba(0,0,0,0) !important;
}
[data-testid="stSidebar"] {
  background: rgba(0,0,0,0.15) !important;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

* {
  font-family: 'Inter', sans-serif;
}

h1, h2, h3 {
  color: #ffffff !important;
  font-family: 'Inter', sans-serif !important;
}

.demo-banner {
  background: rgba(251, 192, 45, 0.15);
  border: 2px solid #FBC02D;
  border-radius: 12px;
  padding: 20px;
  margin: 20px 0;
  text-align: center;
}

.help-tooltip {
  background: rgba(95, 107, 255, 0.1);
  border-left: 4px solid #5f6bff;
  padding: 12px;
  border-radius: 8px;
  margin: 10px 0;
  font-size: 13px;
}

.upload-section {
  background: rgba(255,255,255,0.03);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 20px;
  border: 1px solid rgba(255,255,255,0.05);
}

.section-header {
  color: #4CAF50;
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 15px;
  letter-spacing: 0.5px;
}

.guidelines-box {
  background: rgba(76, 175, 80, 0.05);
  border-left: 4px solid #4CAF50;
  padding: 15px;
  border-radius: 8px;
  margin: 20px 0;
}

.warning-box {
  background: rgba(251, 192, 45, 0.05);
  border-left: 4px solid #FBC02D;
  padding: 15px;
  border-radius: 8px;
  margin: 20px 0;
}

.stButton button {
  background: #4CAF50 !important;
  color: white !important;
  border: none !important;
  border-radius: 8px !important;
  padding: 12px 32px !important;
  font-weight: 600 !important;
  font-size: 16px !important;
  transition: all 0.3s ease !important;
}

.stButton button:hover {
  background: #66BB6A !important;
  transform: scale(1.02);
}

.status-badge {
  display: inline-block;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.status-pending {
  background: rgba(251, 192, 45, 0.2);
  color: #FDD835;
}

.status-complete {
  background: rgba(76, 175, 80, 0.2);
  color: #66BB6A;
}

p, label, div {
  color: #8b92a8 !important;
}

.stFileUploader label {
  color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'uploads' not in st.session_state:
    st.session_state.uploads = {}

# Header
st.markdown("""
<div style="text-align:center; margin-bottom:30px;">
  <h1 style="font-family:'Inter', sans-serif; font-weight:800; color:#ffffff; font-size:48px; margin-bottom:5px; letter-spacing:-1px;">
    FluX-Tape / Artist Dashboard
  </h1>
  <h3 style="font-family:'Inter', sans-serif; font-weight:400; color:#8b92a8; font-size:16px; margin-top:0; letter-spacing:0.5px;">
    Turn Your Song into a Probability Cloud
  </h3>
</div>
""", unsafe_allow_html=True)

# DEMO BANNER
st.markdown("""
<div class="demo-banner">
  <h3 style="color:#FBC02D; font-size:20px; margin-bottom:10px;">⚠️ DEMO PROTOTYPE</h3>
  <p style="color:#8b92a8; font-size:14px; margin:0;">
    This is a demonstration interface. Files you upload here are <strong>not saved</strong>.<br>
    Complete the survey to get access to a fully functional version for testing.
  </p>
</div>
""", unsafe_allow_html=True)

# Artist Info Section with tooltip
st.markdown("""
<div class="help-tooltip">
  💡 <strong>Basic Track Info:</strong> Fill in details about your song. This helps organize your stems and sets the contributor period (how long fans can submit versions).
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.text_input("Artist Name", value="Zlisterr", key="artist_name")
    st.text_input("Track Title", placeholder="Enter track name", key="track_title")

with col2:
    st.date_input("Release Date", value=datetime(2026, 1, 15), key="release_date")
    st.selectbox("Genre", ["Hip-Hop", "R&B", "Pop", "Electronic", "Rock", "Other"], key="genre")

with col3:
    st.number_input("BPM", min_value=60, max_value=200, value=120, key="bpm")
    st.number_input("Contributor Period (Days)", min_value=1, max_value=60, value=14, key="contributor_days", 
                    help="How many days contributors can submit their versions")

# Guidelines
st.markdown("""
<div class="guidelines-box">
  <h3 style="color:#4CAF50; font-size:16px; margin-bottom:10px;">📋 STEM UPLOAD GUIDELINES</h3>
  <ul style="color:#8b92a8; font-size:14px; line-height:1.8;">
    <li><strong>Same Length:</strong> All stems must be the exact same duration</li>
    <li><strong>Section Division:</strong> Organize by song sections (verse, chorus, bridge, etc.)</li>
    <li><strong>Mixing:</strong> Avoid heavy master-bus processing - leave headroom for the adaptive mixing engine</li>
    <li><strong>Format:</strong> WAV or AIFF, 24-bit, 48kHz minimum</li>
    <li><strong>Naming:</strong> Use format: [Feature]_[Section]_[Version] (e.g., "Vocals_Verse1_A.wav")</li>
  </ul>
</div>
""", unsafe_allow_html=True)

# Song Structure with tooltip
st.markdown("<h2 style='margin-top:40px;'>Song Structure</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="help-tooltip">
  💡 <strong>How this works:</strong> Define your song's structure (verse, chorus, etc.). Each section can have multiple stem versions. Contributors will mix and match these to create their own take on your song.
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='color:#8b92a8;'>Define your song sections in order</p>", unsafe_allow_html=True)

num_sections = st.number_input("Number of Sections", min_value=1, max_value=10, value=4, key="num_sections")

sections = []
cols = st.columns(min(4, num_sections))
for i in range(num_sections):
    with cols[i % 4]:
        section_name = st.selectbox(
            f"Section {i+1}",
            ["Intro", "Verse", "Pre-Chorus", "Chorus", "Bridge", "Solo", "Breakdown", "Outro"],
            key=f"section_{i}"
        )
        sections.append(section_name)

# Features and Upload Areas
st.markdown("<h2 style='margin-top:40px;'>Upload Stems by Feature</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="help-tooltip">
  💡 <strong>Stems by Feature:</strong> Upload different musical elements separately. Each feature can have multiple versions (e.g., Lyrics A, B, C). Contributors will mix these to create their version.
</div>
""", unsafe_allow_html=True)

features = [
    ("🎤 VOCALS (LYRICS)", "vocals", "Main vocal tracks with lyrics - upload alternate lyric versions", 
     "Upload different lyrical takes here. Listeners can switch between versions while streaming."),
    ("🥁 GROOVE", "groove", "Drum patterns and rhythmic elements - upload alternate groove sections",
     "Different drum patterns or rhythmic variations. Contributors can swap these to change the feel."),
    ("🎸 SOLO", "solo", "Lead instrument solos - upload different takes",
     "Multiple solo takes. Each listener might hear a different solo on each playthrough."),
    ("🎹 INSTRUMENTAL BED", "instrumental", "Harmonic foundation (keys, bass, pads, etc.)",
     "The harmonic core of your song. Upload alternate arrangements or instrumentation."),
    ("🎵 BACKING VOCALS", "backing_vocals", "Background vocals, harmonies, ad-libs",
     "Background vocals and harmonies. Contributors can toggle these on/off or swap versions."),
]

for feature_name, feature_key, description, tooltip in features:
    with st.expander(f"**{feature_name}**", expanded=False):
        st.markdown(f"<div class='section-header'>{feature_name}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#8b92a8; font-size:14px; margin-bottom:10px;'>{description}</p>", unsafe_allow_html=True)
        
        # Feature-specific tooltip
        st.markdown(f"""
        <div class="help-tooltip">
          💡 {tooltip}
        </div>
        """, unsafe_allow_html=True)
        
        # Number of versions for this feature
        num_versions = st.number_input(
            f"Number of alternate versions",
            min_value=1,
            max_value=5,
            value=1,
            key=f"{feature_key}_versions",
            help="How many different versions of this element do you have?"
        )
        
        # Create tabs for each version
        if num_versions > 1:
            version_tabs = st.tabs([f"Version {chr(65+i)}" for i in range(num_versions)])
        else:
            version_tabs = [st.container()]
        
        for v_idx, tab in enumerate(version_tabs):
            with tab:
                version_label = chr(65 + v_idx) if num_versions > 1 else "Main"
                
                # Upload for each section
                st.markdown(f"<p style='color:#ffffff; font-weight:600; margin-top:10px;'>Upload for each section:</p>", unsafe_allow_html=True)
                
                # Demo reminder
                st.markdown(f"""
                <p style='color:#FBC02D; font-size:12px; font-style:italic; margin-bottom:15px;'>
                  ⚠️ Demo only - files won't actually be saved
                </p>
                """, unsafe_allow_html=True)
                
                section_cols = st.columns(min(3, len(sections)))
                for s_idx, section in enumerate(sections):
                    with section_cols[s_idx % 3]:
                        uploaded_file = st.file_uploader(
                            f"{section}",
                            type=["wav", "aiff", "mp3"],
                            key=f"{feature_key}_{version_label}_{section}_{s_idx}",
                            label_visibility="visible"
                        )
                        if uploaded_file:
                            # Store in session state
                            upload_key = f"{feature_key}_{version_label}_{section}"
                            st.session_state.uploads[upload_key] = {
                                'file': uploaded_file,
                                'size': uploaded_file.size,
                                'name': uploaded_file.name
                            }
                            st.markdown(
                                f"<span class='status-badge status-complete'>✓ {uploaded_file.name[:20]}...</span>",
                                unsafe_allow_html=True
                            )

# Special features section
st.markdown("<h2 style='margin-top:40px;'>Additional Features</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="help-tooltip">
  💡 <strong>Spatialization:</strong> Upload different stereo mixes (narrow 60s-style vs wide modern). Listeners can toggle between spatial presentations.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.expander("**🎛️ SPATIALIZATION (Mixing)**", expanded=False):
        st.markdown("<div class='section-header'>🎛️ SPATIALIZATION</div>", unsafe_allow_html=True)
        st.markdown("<p style='color:#8b92a8;'>Upload different spatial mixes (narrow/wide stereo imaging)</p>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <p style='color:#FBC02D; font-size:12px; font-style:italic; margin-bottom:15px;'>
          ⚠️ Demo only - files won't actually be saved
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("**Narrow Mix (60s Vibe)**")
        for s_idx, section in enumerate(sections):
            narrow_file = st.file_uploader(
                f"{section}",
                type=["wav", "aiff", "mp3"],
                key=f"narrow_{section}_{s_idx}"
            )
        
        st.markdown("**Wide Mix (Modern)**")
        for s_idx, section in enumerate(sections):
            wide_file = st.file_uploader(
                f"{section}",
                type=["wav", "aiff", "mp3"],
                key=f"wide_{section}_{s_idx}"
            )

with col2:
    with st.expander("**🎼 REFERENCE MIX**", expanded=False):
        st.markdown("<div class='section-header'>🎼 REFERENCE MIX</div>", unsafe_allow_html=True)
        st.markdown("<p style='color:#8b92a8;'>Upload a reference mix (optional - helps contributors understand your vision)</p>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <p style='color:#FBC02D; font-size:12px; font-style:italic; margin-bottom:15px;'>
          ⚠️ Demo only - files won't actually be saved
        </p>
        """, unsafe_allow_html=True)
        
        ref_mix = st.file_uploader(
            "Full Track Reference",
            type=["wav", "aiff", "mp3"],
            key="reference_mix"
        )

# Upload Summary
st.markdown("<h2 style='margin-top:40px;'>Upload Summary</h2>", unsafe_allow_html=True)

total_uploads = len(st.session_state.uploads)
if total_uploads > 0:
    st.markdown(
        f"<div class='status-badge status-complete'>✓ {total_uploads} files uploaded (demo only)</div>",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        "<div class='status-badge status-pending'>⚠ No files uploaded yet</div>",
        unsafe_allow_html=True
    )

# Action buttons - disabled for demo
st.markdown("<div style='margin-top:30px;'></div>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

with col1:
    if st.button("💾 Save Draft (Demo)", use_container_width=True, disabled=True):
        pass

with col2:
    if st.button("👁️ Preview (Demo)", use_container_width=True, disabled=True):
        pass

with col3:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.uploads = {}
        st.rerun()

with col4:
    if st.button("🚀 Publish (Demo)", use_container_width=True, type="primary", disabled=True):
        pass

# Footer info
st.markdown("""
<div style="text-align:center; margin-top:60px; padding:20px; background:rgba(255,255,255,0.02); border-radius:12px;">
  <div style="color:#8b92a8; font-size:13px; font-family:'Inter', sans-serif; margin-bottom:10px; font-weight:600;">
    💡 WHAT YOU JUST SAW
  </div>
  <div style="color:#6b7280; font-size:12px; font-family:'Inter', sans-serif; line-height:1.6;">
    This is how artists would upload modular stems and define which versions listeners can toggle between.<br>
    The platform automatically detects alternate versions based on uploads.<br><br>
    <strong style="color:#4CAF50;">Want to try the real thing?</strong><br>
    Complete the survey and opt-in to receive a fully functional prototype when it's ready.
  </div>
</div>
""", unsafe_allow_html=True)