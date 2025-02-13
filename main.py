import streamlit as st

# 첫 번째 선택: 지원 유형 선택
st.title("어떤 종류의 지원을 받고 싶나요?")

support_type = st.radio("지원 유형 선택", ["CAT tool", "서버/네트워크/Windows", "MS365", "기타", "테스트"])

# 사용자가 'CAT tool'을 선택한 경우에만 Trados 이슈 목록 표시
if support_type == "CAT tool":
    st.subheader("어떤 Trados 이슈인지 선택해 주세요.")

    trados_issue = st.radio(
        "Trados 이슈 선택",
        ["프로젝트 생성 이슈", "프로젝트 설정 이슈", "클린업 파일 이슈", "파일 손상 이슈", "Add-in, 플러그인 이슈"]
    )

    st.success(f"선택한 이슈: {trados_issue}")

if support_type == "서버/네트워크/Windows":
    st.subheader("어떤 서버/네트워크/Windows 이슈인지 선택해 주세요.")

    trados_issue = st.radio(
        "서버/네트워크/Windows 이슈 선택",
        ["인터넷 속도 느림", "네트워크 드라이브 이슈", "Windows 이슈"]
    )

    st.success(f"선택한 이슈: {trados_issue}")