const api_key = '004cec9b7c88f5147cc4368e4f4fa39b';
const ciudad = 'Santiago';
let lang = 'es';
const url = `https://api.openweathermap.org/data/2.5/weather?q=${ciudad}&units=metric&appid=${api_key}&lang=${lang}`;

fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById('description').innerHTML = data.weather[0].description;
        document.getElementById('temp').innerHTML = `${data.main.temp}°C`;
        document.getElementById('humidity').innerHTML = `Humedad: ${data.main.humidity}%`;
        const iconCode = data.weather[0].icon;
        const iconUrl = `http://openweathermap.org/img/w/${iconCode}.png`;
        document.getElementById('iconClima').src = iconUrl;
    })
    .catch(error => console.error(error));








    const time = document.getElementById('time');
const date = document.getElementById('date');

const monthNames = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septtiembre", "Octubre", "Noviembre", "Deciembre"
];

const interval = setInterval(() => {

    const local = new Date();
    
    let day = local.getDate(),
        month = local.getMonth(),
        year = local.getFullYear();

    time.innerHTML = local.toLocaleTimeString();
    date.innerHTML = `${day} ${monthNames[month]} ${year}`;

}, 1000);

/* Modo oscuro */
const switchButton = document.getElementById('switch');
switchButton.addEventListener('click',()=>{
    document.body.classList.toggle('dark');
    switchButton.classList.toggle('active')
})