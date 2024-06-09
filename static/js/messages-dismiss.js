document.addEventListener('DOMContentLoaded', function () {
    setTimeout(function () {
        let alerts = document.querySelectorAll('.alert-dismissible');
        console.log(alerts); // Log the selected elements
        alerts.forEach(function (alert) {
            let bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 3000); // 3000ms = 3 seconds
});