import streamlit as st

# 첫 번째 선택: 지원 유형 선택
st.title("어떤 종류의 지원을 받고 싶나요?")

# 기본값을 None으로 설정하여 자동 선택을 방지
support_type = st.radio("지원 유형 선택", ["CAT Tool", "서버/네트워크/Windows", "MS365", "기타", "테스트"], index=None)

# 사용자가 'CAT tool'을 선택한 경우에만 관련 목록 표시
if support_type == "CAT Tool":
    st.subheader("어떤 이슈인지 선택해 주세요.")

    cat_issue = st.radio(
        "CAT Tool 종류",
        ["Trados", "Phrase", "MemoQ", "Passolo", "Xbench", "Across/Catalyst"], index=None)


    if cat_issue == "Trados":
        trados_issue = st.radio(
            "Trados 이슈",
            ["라이선스", "프로젝트 생성/설정", "Add-in/Plug-in", "태그 제작", "기타"], index=None)

        if trados_issue == "라이선스":
            license_issue = st.radio(
                "라이선스",
                ["No license type found 오류", "Evaluation Expired [37] 오류"], index=None)

            if license_issue == "No license type found 오류":
                st.write("이전 버전의 라이선스 정보가 레지스트리에 등록되어 있습니다.<br>"
                         "레지스트리 편집기 실행: Windows 키 + R > regedit 입력 후 확인<br>"
                         "레지스트리 경로: 컴퓨터\\HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\Trados\\Studio17License<br>"
                         "경로 내 'CheckedOutEdition' 데이터 값을 'WorkgroupEdition'으로 수정해 주세요.<br><br> 해결되지 않을 경우 아래 링크를 통해 지원 요청 부탁드립니다.", unsafe_allow_html=True)
                st.markdown("[지원 요청하기](https://globalway.sharepoint.com/_layouts/15/listform.aspx?PageType=8&ListId=%7B5B0294C8-DF48-469F-92E1-3311A6F850EA%7D&RootFolder=%2FLists%2FSupport&Source=https%3A%2F%2Fglobalway.sharepoint.com%2FLists%2FSupport%2FAllItems.aspx%3FsortField%3D%255Fxc644%255F%255Fxb8cc%255F%255Fx0020%255F%255Fxc2dc%255F%255Fxac%26isAscending%3Dfalse%26groupBy%3D%255Fxc885%255F%255Fxb958%255F%26viewid%3D3a277bcd%252De09e%252D43f9%252Dbfe8%252D7ae30421cc89%26view%3D7%26q%3D%25EB%259D%25BC%25EC%259D%25B4%25EC%2584%25A0%25EC%258A%25A4&ContentTypeId=0x010080F3A6FBB7256143AA68746BF8C8EDF5)")

        if trados_issue == "프로젝트 생성/설정":
            project_issue = st.radio(
                "프로젝트 생성/설정",
                ["System.OutOfMemoryException 오류 발생", "리턴 패키지 XLIFF 유효성 오류 발생"], index=None)

            # 여기에 프로젝트 관련 이슈를 처리하는 코드를 추가할 수 있습니다.
            if project_issue == "System.OutOfMemoryException 오류 발생":
                st.write("해당 오류는 시스템 메모리가 부족할 때 발생합니다. 메모리를 확보하거나 시스템 설정을 조정해 주세요.")
            elif project_issue == "리턴 패키지 XLIFF 유효성 오류 발생":
                st.write("XLIFF 파일의 유효성을 확인해 주세요. 잘못된 형식이 포함되어 있을 수 있습니다.")

if support_type == "서버/네트워크/Windows":
    st.subheader("어떤 서버/네트워크/Windows 이슈인지 선택해 주세요.")

    cat_issue = st.radio(
        "서버/네트워크/Windows 이슈",
        ["인터넷 속도 느림", "네트워크 드라이브 이슈", "Windows 이슈"], index=None)


    st.success(f"선택한 이슈: {cat_issue}")
