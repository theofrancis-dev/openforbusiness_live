document.addEventListener('DOMContentLoaded', function() {
    
    //e stand for Element
    //b stand for business
    
    eCard = document.getElementById('bCard');
    businessName = document.getElementById('label_new_name');
    business_name_cont = document.getElementById('label_new_name_div');

    eCardStyle = document.getElementById('card_style');
    eCardStyle.style.backgroundColor = document.getElementById('option-201').style.backgroundColor;

    divAddress = document.getElementById('div_address_id');
    description1 = document.getElementById('description1');
    description2 = document.getElementById('description2');
    des_ctnr = document.getElementById('des_ctnr');
    address_label = document.getElementById('address_label_id');
    address_label.style.color = '#e60000';    
    eCardStyle.onchange= showCardStyle;   
 }
 )

 let showCardStyle = function () {
    bg_top = this.options[this.selectedIndex].dataset.bg_top;
    txt_top = this.options[this.selectedIndex].dataset.txt_top;
    //center
    bg_center = this.options[this.selectedIndex].dataset.bg_center;    
    txt_center = this.options[this.selectedIndex].dataset.txt_center;
    //bottom
    bg_bottom = this.options[this.selectedIndex].dataset.bg_bottom;
    txt_bottom = this.options[this.selectedIndex].dataset.txt_bottom;

    iconsColor  = this.options[this.selectedIndex].dataset.iconscolor;
    
    //card style selector
    eCardStyle.style.backgroundColor = bg_top;
    eCardStyle.style.color = txt_top;
    
    //top business name
    businessName.style.backgroundColor = bg_top;        
    businessName.style.color = txt_top;
    business_name_cont.style.backgroundColor = bg_top;

    //center
    des_ctnr.style.backgroundColor = bg_center;
    description1.style.backgroundColor = bg_center;
    description1.style.color = txt_center;
    description2.style.backgroundColor = bg_center;
    description2.style.color = txt_center;

    //bottom
    divAddress.style.backgroundColor = bg_bottom;
    address_label.style.color = txt_bottom;
}

function changeLabelName ( element, container){
    let txt = element.value;
    console.log(`txt: ${txt}`);
    document.getElementById(container).textContent = txt;    
}