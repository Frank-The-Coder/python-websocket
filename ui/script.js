const alertQueue = [];
let isAlertVisible = false;

document.getElementById('trigger-alert').addEventListener('click', function() {
    // 示例消息，实际使用时可替换为动态消息
    addAlertToQueue('张三', '这是一个测试消息内容。');
    addAlertToQueue('李四', '这是另一个测试消息内容。');
    processQueue();
});

document.getElementById('close-btn').addEventListener('click', function() {
    closeAlert();
});

document.getElementById('dismiss-btn').addEventListener('click', function() {
    closeAlert();
});

function addAlertToQueue(sender, message) {
    alertQueue.push({ sender, message });
}

function processQueue() {
    if (!isAlertVisible && alertQueue.length > 0) {
        const alert = alertQueue.shift();
        showAlert(alert.sender, alert.message);
    }
}

function showAlert(sender, message) {
    isAlertVisible = true;
    const alertPopup = document.getElementById('alert-popup');
    document.getElementById('sender').textContent = sender;
    document.getElementById('message-content').textContent = message;
    alertPopup.classList.remove('hidden');
    alertPopup.classList.add('visible');
}

function closeAlert() {
    const alertPopup = document.getElementById('alert-popup');
    alertPopup.classList.remove('visible');
    alertPopup.classList.add('hidden');
    setTimeout(() => {
        isAlertVisible = false;
        processQueue();
    }, 500); // 动画持续时间应与CSS中的transition一致
}
