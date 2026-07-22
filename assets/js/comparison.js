/* ==========================================================================
   VOLTAGE — comparison.js
   Handles: Product comparison tool (select up to 4, render spec table).
   ========================================================================== */

(function () {
  "use strict";

  const SPEC_SETS = {
    "Laptops": ["Processor", "RAM", "Storage", "Display", "GPU", "Battery Life", "Weight"],
    "Smartphones": ["Chipset", "RAM", "Storage", "Display", "Camera", "Battery", "5G"],
    "Headphones": ["Driver Size", "Battery Life", "ANC", "Connectivity", "Weight", "Water Resistance"],
    "Smartwatches": ["Display", "Battery Life", "GPS", "Water Resistance", "Sensors", "Compatibility"],
    "Gaming": ["Processor", "GPU", "RAM", "Storage", "Refresh Rate", "Ports"],
    "Accessories": ["Type", "Connectivity", "Compatibility", "Warranty"]
  };

  function fakeSpec(product, spec) {
    // Deterministic pseudo-spec generator so values look consistent across reloads
    const seedNum = product.id * 7 + spec.length;
    const table = {
      "Processor": ["Intel Core Ultra 9", "AMD Ryzen 9", "Apple M4 Pro", "Intel Core i7"],
      "RAM": ["16GB", "32GB", "8GB", "64GB"],
      "Storage": ["512GB SSD", "1TB SSD", "2TB SSD", "256GB SSD"],
      "Display": ["14\" 2.8K OLED", "16\" 4K Mini-LED", "6.7\" AMOLED 120Hz", "1.4\" AMOLED"],
      "GPU": ["RTX 5070", "RTX 5080", "Integrated Graphics", "RTX 5090"],
      "Battery Life": ["Up to 18 hrs", "Up to 24 hrs", "Up to 30 hrs", "Up to 8 hrs"],
      "Weight": ["1.4 kg", "1.9 kg", "220 g", "48 g"],
      "Chipset": ["Snapdragon 8 Elite", "A18 Pro", "Dimensity 9400"],
      "Camera": ["50MP Triple", "48MP Dual", "108MP Quad"],
      "Battery": ["4500 mAh", "5000 mAh", "3800 mAh"],
      "5G": ["Yes", "Yes", "No"],
      "Driver Size": ["40mm", "50mm", "10mm"],
      "ANC": ["Adaptive ANC", "Hybrid ANC", "No ANC"],
      "Connectivity": ["Bluetooth 5.4", "USB-C + BT 5.3", "Wi-Fi 6E"],
      "Water Resistance": ["IPX4", "IP68", "None"],
      "GPS": ["Built-in GPS", "Connected GPS", "No GPS"],
      "Sensors": ["Heart Rate + SpO2", "ECG + Heart Rate", "Basic Accelerometer"],
      "Compatibility": ["iOS + Android", "Android Only", "iOS Only"],
      "Refresh Rate": ["165Hz", "240Hz", "360Hz"],
      "Ports": ["USB-C, HDMI 2.1, 3x USB-A", "USB-C, HDMI, Ethernet"],
      "Type": ["Wired", "Wireless", "Hybrid"],
      "Warranty": ["1 Year", "2 Years", "3 Years"]
    };
    const options = table[spec] || ["Standard"];
    return options[seedNum % options.length];
  }

  function initComparison() {
    const root = document.querySelector("[data-comparison-tool]");
    if (!root) return;
    const PRODUCTS = window.VOLTAGE_PRODUCTS || [];
    const picker = root.querySelector("[data-compare-picker]");
    const tableWrap = root.querySelector("[data-compare-table]");
    const emptyMsg = root.querySelector("[data-compare-empty]");
    const clearBtn = root.querySelector("[data-compare-clear]");
    const catSelect = root.querySelector("[data-compare-category]");

    let selected = [];

    function renderPicker() {
      const cat = catSelect ? catSelect.value : "Laptops";
      const options = PRODUCTS.filter(p => p.cat === cat);
      picker.innerHTML = options.map(p => {
        const isActive = selected.includes(p.id);
        const isDisabled = selected.length >= 4 && !isActive;
        return `
        <label class="compare-picker__item ${isActive ? "active" : ""} ${isDisabled ? "disabled" : ""}">
          <input type="checkbox" value="${p.id}" ${isActive ? "checked" : ""} ${isDisabled ? "disabled" : ""} style="display:none;">
          <div class="compare-picker__media">
            ${p.badge ? `<span class="badge badge-${p.badge} compare-picker__badge">${p.badge}</span>` : ''}
            <div class="compare-picker__check">
              ${isActive ? '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>' : ''}
            </div>
            <img src="${p.img}" alt="${p.name}" loading="lazy">
          </div>
          <div class="compare-picker__body">
            <span class="compare-picker__cat">${p.brand || cat} · ${p.sub || 'Tech'}</span>
            <h3 class="compare-picker__title">${p.name}</h3>
            <div class="compare-picker__price">
              <span>$${p.price.toLocaleString()}</span>
              ${p.was ? `<span style="text-decoration:line-through;color:var(--text-muted);font-size:0.85em;margin-left:auto;">$${p.was.toLocaleString()}</span>` : ''}
            </div>
          </div>
        </label>`;
      }).join("");
    }

    function renderTable() {
      if (!selected.length) {
        tableWrap.innerHTML = "";
        emptyMsg.style.display = "block";
        return;
      }
      emptyMsg.style.display = "none";
      const products = selected.map(id => PRODUCTS.find(p => p.id === id)).filter(Boolean);
      const cat = products[0].cat;
      const specs = SPEC_SETS[cat] || [];

      let html = `<div class="table-wrap"><table class="data-table compare-table"><thead><tr><th>Specification</th>`;
      products.forEach(p => {
        html += `<th><div style="display:flex;flex-direction:column;gap:8px;align-items:flex-start;">
          <img src="${p.img}" alt="${p.name}" loading="lazy" width="90" height="68" style="border-radius:8px;object-fit:cover;">
          <span>${p.name}</span>
          <span class="badge badge-primary">$${p.price.toLocaleString()}</span>
        </div></th>`;
      });
      html += `</tr></thead><tbody>`;
      specs.forEach(spec => {
        html += `<tr><td style="font-weight:600;">${spec}</td>`;
        products.forEach(p => { html += `<td>${fakeSpec(p, spec)}</td>`; });
        html += `</tr>`;
      });
      html += `<tr><td style="font-weight:600;">Rating</td>`;
      products.forEach(p => { html += `<td>⭐ ${p.rating} / 5</td>`; });
      html += `</tr></tbody></table></div>`;
      tableWrap.innerHTML = html;
    }

    picker.addEventListener("change", e => {
      const input = e.target.closest("input");
      if (!input) return;
      const id = Number(input.value);
      if (input.checked) {
        if (selected.length >= 4) { input.checked = false; return; }
        selected.push(id);
      } else {
        selected = selected.filter(i => i !== id);
      }
      renderPicker();
      renderTable();
    });

    catSelect && catSelect.addEventListener("change", () => {
      selected = [];
      renderPicker();
      renderTable();
    });

    clearBtn && clearBtn.addEventListener("click", () => {
      selected = [];
      renderPicker();
      renderTable();
    });

    // Hash-based preload: #compare=1,2,3
    const hashMatch = window.location.hash.match(/compare=([\d,]+)/);
    if (hashMatch) {
      selected = hashMatch[1].split(",").map(Number).slice(0, 4);
    }

    renderPicker();
    renderTable();
  }

  document.addEventListener("DOMContentLoaded", initComparison);
})();
