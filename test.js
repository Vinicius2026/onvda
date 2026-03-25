const puppeteer = require('puppeteer');
(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('http://localhost:8081/index.html');
    
    const info = await page.evaluate(() => {
        let el = document.getElementById('dashboard-presentation');
        let data = [];
        while(el && el.tagName !== 'HTML') {
            const comp = window.getComputedStyle(el);
            data.push({
                tag: el.tagName,
                id: el.id,
                className: el.className,
                w: comp.width,
                maxW: comp.maxWidth,
                pl: comp.paddingLeft,
                pr: comp.paddingRight,
                ml: comp.marginLeft,
                mr: comp.marginRight
            });
            el = el.parentElement;
        }
        return data;
    });
    console.log(JSON.stringify(info, null, 2));
    await browser.close();
})();
