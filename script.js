document.onreadystatechange = () => {
    if (document.readyState === 'complete') {
        const doc = window.parent.document;
        doc.querySelector('.css-1qrvfrg').addEventListener('click', function() {
        doc.querySelectorAll('.css-9s5bis')[1].click(); // same behavior as doc.querySelector('[role="combobox"]').click()
        });
    }
};

