// DOM refs
const brandSelect = document.getElementById("brand");
const modelSelect = document.getElementById("model");
const logoImg     = document.getElementById("brandLogo");
const buyWrap     = document.getElementById("buyingPriceContainer");
const form        = document.getElementById("predictForm");
const resetBtn    = document.getElementById("resetBtn");

// Brand -> Models
const brandModels = {
  "Maruti": ["Swift","Baleno","Dzire","Wagon R","Ertiga"],
  "Hyundai":["i20","Creta","Venue","Verna","Santro"],
  "Tata":   ["Nexon","Altroz","Punch","Harrier"],
  "Honda":  ["City","Amaze","Jazz"],
  "Mahindra":["Thar","Scorpio","XUV700"],
  "Toyota": ["Fortuner","Innova Crysta","Glanza"],
  "BMW":    ["3 Series","5 Series","X1"],
  "Audi":   ["A4","A6","Q3"],
  "Mercedes-Benz":["C-Class","E-Class","GLA"]
};

// Logos mapping
const logos = {
  "Maruti":"maruti.png","Hyundai":"hyundai.png","Tata":"tata.png",
  "Honda":"honda.png","Mahindra":"mahindra.png","Toyota":"toyota.png",
  "BMW":"bmw.png","Audi":"audi.png","Mercedes-Benz":"mercedes.png"
};

// On load: hydrate logo and model list from existing values (post-prediction persistence)
(function initOnLoad(){
  if (!brandSelect) return;
  const b = brandSelect.value;
  // set logo to current brand (kept between predictions)
  logoImg.src = `/static/logos/${logos[b] || "default.png"}`;

  // model dropdown
  if (b === "Others") {
    modelSelect.style.display = "none";
    buyWrap.style.display = "block";
  } else {
    buyWrap.style.display = "none";
    modelSelect.style.display = "block";
    // if only placeholder exists, populate choices
    if (modelSelect.options.length <= 1 && brandModels[b]) {
      brandModels[b].forEach(m=>{
        const opt=document.createElement("option");
        opt.value=m; opt.textContent=m; modelSelect.appendChild(opt);
      });
    }
  }
})();

// Brand change: update logo, show/hide model vs buying price
brandSelect?.addEventListener("change", () => {
  const b = brandSelect.value;
  logoImg.src = `/static/logos/${logos[b] || "default.png"}`;

  if (b === "Others") {
    modelSelect.style.display = "none";
    buyWrap.style.display = "block";
  } else {
    buyWrap.style.display = "none";
    modelSelect.style.display = "block";
    modelSelect.innerHTML = '<option value="">Select Model</option>';
    (brandModels[b] || []).forEach(m=>{
      const opt=document.createElement("option");
      opt.value=m; opt.textContent=m; modelSelect.appendChild(opt);
    });
    // soft fade
    modelSelect.style.opacity = "0";
    setTimeout(()=>{ modelSelect.style.opacity = "1"; modelSelect.style.transition = ".35s"; }, 60);
  }
});

// Subtle card bounce on submit
form?.addEventListener("submit", () => {
  if (window.gsap) gsap.to(".card",{scale:1.02,duration:.16,yoyo:true,repeat:1});
});

// Reset: also reset logo to default (only here)
resetBtn?.addEventListener("click", () => {
  // navigation to "/" will clear, but we also snap the logo visually
  if (logoImg) logoImg.src = `/static/logos/default.png`;
});
