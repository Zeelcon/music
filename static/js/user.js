/*
    Logic：
        主要采用原生 JavaScript，
        只有在发送 Ajax 请求是才使用 JQuery

    ===
    1、登录注册页面的切换逻辑

    2、Ajax发送及接受响应逻辑
    ===
*/



// 封装选择器, 采用ES6箭头函数写法
const getSelector = ele => {
    return typeof ele === "string" ? document.querySelector(ele) : "";
};


// 登录注册载入

const containerShow = () => {
    var show = getSelector(".container");
    show.className += " container-show";
};


window.onload = containerShow;


// 登录注册页切换
((window, document) => {

    // 登录 -> 注册 -> 找回密码
    let toSignBtn = getSelector(".toSign"),
        toLoginBtn = getSelector(".toLogin"),
        // toForgetBtn = getSelector(".toForget"),
        loginBox = getSelector(".login-box"),
        signBox = getSelector(".sign-box")
        // forgetBox = getSelector(".forget-box")
        ;

    toSignBtn.onclick = () => {
        loginBox.className += ' animate_login';
        signBox.className += ' animate_sign';
        // forgetBox.className += 'animate_forget'
        // ;
    };

    toLoginBtn.onclick = () => {
        loginBox.classList.remove("animate_login");
        signBox.classList.remove("animate_sign");
    }
/*
    toForgetBtn.onclick = () => {
        loginBox.classList.remove("animate_login");
        forgetBox.classList.remove("animate_forget");
    }
*/

})(window, document);

// Ajax 请求发送
