function waitForElement(selector) {
    return new Promise((resolve) => {
        if (document.querySelector(selector)) {
            return resolve(document.querySelector(selector));
        }

        const observer = new MutationObserver((mutations) => {
            if (document.querySelector(selector)) {
                resolve(document.querySelector(selector));
                observer.disconnect();
            }
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true,
        });
    });
}

function setupMasonry($grid) {
    // var $grid = document.querySelector(".cn_row");
    var msnry = new Masonry($grid, {
        itemSelector: ".cn_col",
        percentPosition: true,
    });
    var $images = $grid.querySelectorAll(".card img");
    Promise.all(
        Array.from($images)
            .filter((img) => !img.complete)
            .map(
                (img) =>
                    new Promise((resolve) => {
                        img.addEventListener("load", resolve);
                        img.addEventListener("error", resolve);
                    })
            )
    ).then(() => {
        msnry.layout();
    });
}
waitForElement(".cn_row").then((elm) => {
    setupMasonry(elm);
});
