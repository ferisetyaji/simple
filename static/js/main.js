$(document).ready(function(){
	$('#myTable').DataTable();
	$('#myTable1').DataTable();
    $('.dataTables_info').remove();
	
	var burger = 0;
	$(document).on('click', '.burger', function(){
		if(burger == 0){
			$('.admin-menu').addClass('side-in');
			$('.contents').addClass('content-in');
			burger++;
		}else{
			$('.admin-menu').removeClass('side-in');
			$('.contents').removeClass('content-in');
			burger--;
		}
	});

	$(document).on('click' , '.drop-bar', function(){
		$('.navbar-img').append('<div class="drop-hide"></div>');
		$('.dropmenu').addClass('dropmenu-ac');
	});
	$(document).on('click', '.drop-hide', function(){
		$(this).remove();
		$('.dropmenu').removeClass('dropmenu-ac');
	});

	var adminmenu = $('#data').attr('data-id');
	$(adminmenu+' .submenu').css({'max-height':'initial'});
	$(adminmenu+' .admin-menu-first').removeClass('admin-menu-first').addClass('admin-menu-active');

	$(document).on('click', '.admin-menu-first', function(){
		var panel = this.nextElementSibling;
		$('.admin-menu-active').removeClass('admin-menu-active').addClass('admin-menu-first');
		$('.submenu').css({'max-height':'0px'});
		$(this).removeClass('admin-menu-first').addClass('admin-menu-active');
		panel.style.maxHeight = panel.scrollHeight + "px";
	});
	$(document).on('click', '.admin-menu-active', function(){
		$('.submenu').css({'max-height':'0px'});
		$('.admin-menu-active').removeClass('admin-menu-active').addClass('admin-menu-first');
	});

	var checkid = document.getElementsByClassName('check');

	function check(){
	    for(var i = 0; i < checkid.length; i++){
	    	checkid[i].checked=true
	    }
	}
	
	function uncheck(){
	    for(var i = 0; i < checkid.length; i++){
	    	checkid[i].checked=false
	    }
	}

	var inputChecked = document.getElementsByClassName('in-check');

	function inputCheck(){
		var inc = [];
		for(var i = 0; i < inputChecked.length; i++){
			var sinc = inputChecked[i].checked;
			if(sinc != false){
				inc[i] = inputChecked[i].value;
			}
		}

		return inc;
	}

	$(document).on('click', '.check-true', function(){
		$('.check-true').removeClass('check-true').addClass('check-false');
		check();
		$('.in-del').val(inputCheck());
	});

	$(document).on('click', '.check-false', function(){
		$('.check-false').removeClass('check-false').addClass('check-true');
		uncheck();
		$('.in-del').val(inputCheck());
	});

	$('.check', this).click(function(){
		$('.check-false').removeClass('check-false').addClass('check-true');
		document.getElementById('all-check').checked=false
		$('.in-del').val(inputCheck());
	});

	$('.add-cart').click(function(){
		var nama = $('.name-cart').val();
		nama = nama.split(",");
		var jml = $('.jml_cart').val();
		var id = Math.floor(Math.random() * 100);
		$('.no-list-cart').remove();
		$('.list-cart').prepend('<tr class="'+id+'"><td>'+nama[0]+'</td><td>'+jml+'</td><td><button type="button" class="btn btn-danger btn-xs del-cart" data-id="'+id+'">Hapus</button></td><input type="hidden" name="produk[]" value="'+nama[0]+'"><input type="hidden" name="harga[]" value="'+nama[1]+'"><input type="hidden" name="jml[]" value="'+jml+'"></tr>');
	});

	var url = 'http://localhost/zerah/user/';

	$('.in-kab').change(function(){
		var id = $('.in-kab').val();
		$.get(url+'kec/'+id, function(data){
			var kec = '<option value="">- Pilih Kecamatan -</option>';
			for(var i = 0; i < data.length; i++){
				kec += '<option value="'+data[i].id_kecamatan+'">'+data[i].nama_kecamatan+'</option>';
			}
			$('.in-kec').html(kec);
		});
	});

	$('.in-kec').change(function(){
		var id = $('.in-kec').val();
		$.get(url+'des/'+id, function(data){
			console.log(data);
			var desa = '<option value="">- Pilih Desa -</option>';
			for(var i = 0; i < data.length; i++){
				desa += '<option value="'+data[i].id_desa+'">'+data[i].nama_desa+'</option>';
			}
			$('.in-desa').html(desa);
		});
	});

	$('.tolak').click(function(){
		var id = $(this).attr('data-id');
		$('.submit-tolak').val(id);
	});

	$('.btn-obat').click(function(){
		var id = $(this).attr('data-id');
		var obat = $(this).attr('data-nama');
		$('.input-obat').val(id);
		$('.view-obat').text(obat);
	});

	$('.pilih-obat').change(function(){
		$('#submit-obat').submit();
	});
});