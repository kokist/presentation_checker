# Presentation Checker

<table>
  <tr>
    <td style="text-align: center;">
      <img src="https://github.com/user-attachments/assets/bb4390c5-d6d2-4d7a-9fc1-667b22c1e6e3" alt="home" width="300"><br>
      <b>home</b>
    </td>
    <td style="text-align: center;">
      <img src="https://github.com/user-attachments/assets/f7e88253-aa87-4545-aedf-b3ade43da4a2" alt="ppt2sound" width="300"><br>
      <b>ppt2sound</b>
    </td>
    <td style="text-align: center;">
      <img src="https://github.com/user-attachments/assets/525c90ca-5a1e-44cb-b706-d194e69a6cba" alt="Q&A with gpt" width="300"><br>
      <b>Q&A with GPT-4o</b>
    </td>
  </tr>
</table>

This app is a pronunciation checker designed for non-native English speakers.   
It extracts speaker notes from PowerPoint and outputs them as audio.   
Additionally, by uploading the presentation slides in PDF format, you can prepare for questions using GPT-4o.

# Installation
```
conda create -n presentation_checker python=3.10
conda activate presentation_checker
pip install -r requirements.txt
```

# How to run
```
$env:OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
streamlit run app.py
```
