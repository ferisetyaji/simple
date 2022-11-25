$(document).ready(function(){
    $('#myTable').DataTable();
    $('#myTable1').DataTable();
    $('.dataTables_info').remove();

    $('.min-qty').click(function(){
    	var id = $(this).attr('data-id');
    	var qty = parseInt($('#nilai-qty-' + id).text());
    	var harga = parseInt($('#harga-' + id).attr('data-harga'));
    	console.log(harga);
    	if(qty > 0){
    		qty--;
    		harga *= qty;
    		var coin = harga > 0 ? numeral(harga).format('0,0'): 0;
    		$('#harga-' + id).text('Rp. ' + coin);
    		$('#nilai-qty-' + id).text(qty);
    		$('#stok-qty-' + id).val(qty);
    	}
    });

    $('.plus-qty').click(function(){
    	var id = $(this).attr('data-id');
    	var qty = parseInt($('#nilai-qty-' + id).text());
    	var harga = parseInt($('#harga-' + id).attr('data-harga'));
    	console.log(harga);
    	qty++;
    	harga *= qty;
    	var coin = harga > 0 ? numeral(harga).format('0,0'): 0;
    	$('#harga-' + id).text('Rp. ' + coin);
    	$('#nilai-qty-' + id).text(qty);
    	$('#stok-qty-' + id).val(qty);
    });
});

countCart();
countOrder();

function countCart(){
    var keranjang = localStorage.getItem('keranjang') != undefined ? JSON.parse(localStorage.getItem('keranjang')): [];
    var jmlKeranjang = 0;
    for(var i = 0; i < keranjang.length; i++){

        jmlKeranjang++;
    }

    document.querySelector('#j-keranjang').innerHTML = jmlKeranjang;
}

function countOrder(){
    var keranjang = localStorage.getItem('pesanan') != undefined ? JSON.parse(localStorage.getItem('pesanan')): [];
    var jmlKeranjang = 0;
    for(var i = 0; i < keranjang.length; i++){

        jmlKeranjang++;
    }

    document.querySelector('#j-pesanan').innerHTML = jmlKeranjang;
}

$(document).on('click', '.plus-cart', function(){
    var data = localStorage.getItem('keranjang') != undefined ? JSON.parse(localStorage.getItem('keranjang')): [];
    var id = $(this).attr('data-id');
    data.push(id);
    var cart_a = [];
    for(var i = 0; i < data.length; i++){
        if(data[i] == id){
            cart_a.push(data[i]);
        }
    }
    $('.jml-cart-'+id).text(cart_a.length);
    $('.jml-cart-'+id).attr('data-jml', cart_a.length);
    data = JSON.stringify(data);
    localStorage.setItem('keranjang', data);
    countCart();
});

$(document).on('click', '.min-cart', function(){
    var data = localStorage.getItem('keranjang') != undefined ? JSON.parse(localStorage.getItem('keranjang')): [];
    var id = $(this).attr('data-id');
    var cart_a = [];
    var cart_b = [];
    for(var i = 0; i < data.length; i++){
        if(data[i] == id){
            cart_a.push(data[i]);
        }else{
            cart_b.push(data[i]);
        }
    }
    if(cart_a.length > 1){
        cart_a.pop();
    }
    $('.jml-cart-'+id).text(cart_a.length);
    $('.jml-cart-'+id).attr('data-jml', cart_a.length);
    var list_cart = [];
    for(var a = 0; a < cart_a.length; a++){
        list_cart.push(cart_a[a]);
    }
    for(var b = 0; b < cart_b.length; b++){
        list_cart.push(cart_b[b]);
    }
    data = JSON.stringify(list_cart);
    localStorage.setItem('keranjang', data);
    countCart();
});

$('.ac-alamat').click(function(){
    var up = $('.fa-chevron-up').attr('class');
    var down = $('.fa-chevron-down').attr('class');
    if(up != undefined){
        $('.fa-chevron-up').removeClass('fa-chevron-up').addClass('fa-chevron-down');
    }
    if(down != undefined){
        $('.fa-chevron-down').removeClass('fa-chevron-down').addClass('fa-chevron-up');
    }
});

