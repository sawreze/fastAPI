
const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json'
    //서버에 보내는 데이터의 형식이JSON이라고 알려주기 위한 값
    let body = JSON.stringify(params)
    //자바스크립트 객체를 JSON 문자열로 변환
    //let _url = 'http://127.0.0.1:8000' + url
    let _url = import.meta.env.VITE_SERVER_URL + url
    //API 호출 주소는 호스트명 (예: http://127.0.0.1:8000)에 전달받은 url 값 (라우터)
    if(method === 'get') {
        _url += "?" + new URLSearchParams(params)//변수를 연결해서 붙이는 역할(params$)
    }
    let options = {
        method: method,
        headers: {
            "Content-Type": content_type
        }
    }
    if (method !== 'get'){
        options['body'] = body
    }
    fatch(_url, options)
        .then(response => {
            response.json()
                .then(json => {
                    if(response.status >= 200 && response.status < 300) {
                        if(success_callback) {
                            success_callback(json)
                        }
                    } else {
                        alert(JSON.stringify(json))
                    }
                })
                .catch(error => {
                    alert(JSON.stringify(error))
                })
        })
}
export default fastapi
