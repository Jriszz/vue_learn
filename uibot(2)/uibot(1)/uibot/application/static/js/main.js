 $(function () {

 				var cacheobj = {}; //设置缓存对象

                $('.dropdown-toggle').dropdown();

                //模块下拉框
                $("#dropdownMenu1").on("click",function(){
                	var modules_res = "";
					$("#names_module").empty();
					$("#names_module").append('<li><i class="fa fa-spinner fa-pulse"></i></li>');
					modules_res = $.data(cacheobj,'module_name');
					if (typeof (modules_res)  == "undefined"){
						$.ajax(
							{
								url:"http://192.168.0.108:5050/modules",
								type:"GET",
								context:"",
								data:{},
								async:true,
								success:function(data){

									if (JSON.stringify(data["modules_name"]) == "[]"){
										$("#names_module").empty();
										$("#names_module").append('<li><a href="#" class="specific_module1">暂无数据...</a></li>');
									}
									else{
										//
										$.data(cacheobj,'module_name',data["modules_name"]);
										$("#names_module").empty();
										$("#names_module").append('<li><a href="#" class="module_menu">'+ '请选择模块名称'+'</a></li>');
										$("#names_module").append('<li><a href="#" class="specific_module">'+'全部' +'</a></li>');
										$.each(data["modules_name"],function (key,value) {
											$("#names_module").append('<li><a href="#" class="specific_module">'+ value +'</a></li>');
										})
									}

								},
								error:function (error) {
									console.error(error);
									$("#names_module").empty();
									$("#names_module").append('<li><span>暂无数据...</span></li>');
								}
							}
						)
					}
                	else{
                		$("#names_module").empty()
                		$("#names_module").append('<li><a href="#" class="module_menu">'+ '请选择模块名称'+'</a></li>');
                		$("#names_module").append('<li><a href="#" class="specific_module">'+ '全部' +'</a></li>');
						$.each(modules_res,function (key,value) {
							$("#names_module").append('<li><a href="#" class="specific_module">'+ value +'</a></li>');
						})
					}

                });

            //上送模块名
			 $("#names_module").on("click",".specific_module", function() {
				 $("#dropdownMenu1").text($(this).text());
				 $("#dropdownMenu1").append('<span class="caret"></span>')
			 });

			//指令下拉框

			 $("#dropdownMenu2").on("click",function(){
			 	//alert($("#dropdownMenu1").text())
				 var orders_res = "";
				 $("#name_orders").empty();
				 orders_res = $.data(cacheobj,$("#dropdownMenu1").text());
				 $("#name_orders").append('<li><i class="fa fa-spinner fa-pulse"></i></li>');
				 if (typeof (orders_res)  == "undefined"){
					 $.ajax(
						 {



							 url:"http://192.168.0.108:5050/orders",
							 type:"GET",
							 context:"",
							 data:{"module_name":$("#dropdownMenu1").text()},
							 async:true,
							 success:function(data){
								 orders_length = data["orders_name"].length;
								 
								 if($("#dropdownMenu1").text() == "全部"){
								 	$("#name_orders").empty();
									$("#name_orders").append('<li><a href="#" class="specific_order">全部</a></li>');
									return;
								 }

								 if (JSON.stringify(data["orders_name"]) == "[]"){
								 	 $("#name_orders").empty();
									 $("#name_orders").append('<li><a href="#" class="specific_module1">暂无数据...</a></li>');
								 }

								 else{
									 //
									 $.data(cacheobj,$("#dropdownMenu1").text(),data["orders_name"]);
									 //清理等待数据
									 $("#name_orders").empty();
									 $("#name_orders").append('<li><a href="#" class="order_menu">'+ '请选择指令名称'+'</a></li>');
									 $("#name_orders").append('<li><a href="#" class="specific_order">'+ '全部'+'</a></li>');
									 $.each(data["orders_name"],function (key,value) {
									 	 
										 $("#name_orders").append('<li><a href="#" class="specific_order">'+ value +'</a></li>');
									 })
								 }

							 },
							 error:function (error) {
								 console.error(error);
								 $("#name_orders").empty();
								 $("#name_orders").append('<li><span>暂无数据...</span></li>');
							 }
						 }
					 )
				 }
				 else{
				 	 //清理等待数据
				 	 $("#name_orders").empty();
				 	 $("#name_orders").append('<li><a href="#" class="order_menu">'+ '请选择指令名称'+'</a></li>');
				 	 $("#name_orders").append('<li><a href="#" class="specific_order">'+ '全部'+'</a></li>');
					 $.each(orders_res,function (key,value) {
					 	 
						 $("#name_orders").append('<li><a href="#" class="specific_order">'+ value +'</a></li>');
					 })
				 }

			 });

			 $("#name_orders").on("click",".specific_order", function() {
				 $("#dropdownMenu2").text($(this).text());
				 $("#dropdownMenu2").append('<span class="caret"></span>');
			 });

			//设置滚动条
			$('#modal-module-ul,#name_orders,#modal-order-ul,#modal-module-ul').niceScroll(
		    	{
		    		cursorcolor: "#ccc",//#CC0071 光标颜色
				    cursoropacitymax: 1, //改变不透明度非常光标处于活动状态（scrollabar“可见”状态），范围从1到0
				    touchbehavior: false, //使光标拖动滚动像在台式电脑触摸设备
				    cursorwidth: "5px", //像素光标的宽度
				    cursorborder: "0", // 游标边框css定义
				    cursorborderradius: "5px",//以像素为光标边界半径
				    autohidemode: true //是否隐藏滚动条
		    	});



			//点击触发执行
			$(".testcase-run-btn").on("click",function(){
				var commit_data = {}
				commit_data["module_name"] = $("#dropdownMenu1").text();
				commit_data["order_name"] = $("#dropdownMenu2").text();
				commit_data["testcase_number"] = $(".test_number").val();

				$.ajax({
					url:"http://192.168.0.108:5050/casedeploy",
					headers:{
						'Accept': 'application/json',
        				'Content-Type':'application/json'
					},
					type:"POST",
					context:"",
					data:JSON.stringify(commit_data),
					async:true,
					success: function(){
						$(".alert").fadeIn().css("class","alert-success");
						$(".alert strong").text("提交成功!");
                        setTimeout(function () { $(".alert").fadeOut(3000);}, 5000);

					},
					error: function(err){
						$(".alert").fadeIn().css("class","alert-warning");
						$(".alert strong").text("提交失败!");
                        setTimeout(function () { $(".alert").fadeOut(3000);}, 5000);
						console.log(err);
					}

				})
			})

			//设置模态框
			$("#TestCaseModal").bind("show.bs.modal",function(){
				var $this = $(this);
		        var $modal_dialog = $this.find('.modal-dialog');
		        // 关键代码，如没将modal设置为 block，则$modala_dialog.height() 为零
		        $this.css('display', 'block');
		        // $("#modal_main").css("overflow",'auto');
		        $modal_dialog.css({'margin-top': Math.max(0, ($(window).height() - $modal_dialog.height()) / 16) });
		         $modal_dialog.css({'margin-left': Math.max(0, ($(window).width() - $modal_dialog.width()) / 3) });
			});
			$(".add_testcase").on("click",function(){

				$("#modal-module-ul,#modal-order-ul,#modal-main,.modal-foot-btn").empty();

			});
			//模态框里，模块查询
			$("#dropdownMenu3").on("click",function(){
                	var modules_res = "";
					$("#modal-module-ul").empty();
					$("#modal-module-ul").append('<li><i class="fa fa-spinner fa-pulse"></i></li>');
					modules_res = $.data(cacheobj,'module_name');
					if (typeof (modules_res)  == "undefined"){
						$.ajax(
							{
								url:"http://192.168.0.108:5050/modules",
								type:"GET",
								context:"",
								data:{},
								async:true,
								success:function(data){

									if (JSON.stringify(data["modules_name"]) == "[]"){
										$("#modal-module-ul").empty();
										$("#modal-module-ul").append('<li><a href="#" class="specific_module1">暂无数据...</a></li>');
									}
									else{
										//取出缓存数据，生成DOM
										$.data(cacheobj,'module_name',data["modules_name"]);
										$("#modal-module-ul").empty();
										$.each(data["modules_name"],function (key,value) {
											$("#modal-module-ul").append('<li><a href="#" class="modal-specific_module">'+ value +'</a></li>');
										})
									}

								},
								error:function (error) {
									console.error(error);
									$("#modal-module-ul").empty();
									$("#modal-module-ul").append('<li><span>暂无数据...</span></li>');
								}
							}
						)
					}
                	else{
                		$("#modal-module-ul").empty()
						$.each(modules_res,function (key,value) {
							$("#modal-module-ul").append('<li><a href="#" class="modal-specific_module">'+ value +'</a></li>');
						})
					}
			});
			
			//选中模态框中的模块
			$("#modal-module-ul").on("click",".modal-specific_module", function() {
				 $("#dropdownMenu3").text($(this).text());
				 $("#dropdownMenu3").append('<span class="caret"></span>');
			 });


			//模态框里，指令查询
			$("#dropdownMenu4").on("click",function(){

				 var orders_res = "";
				 $("#modal-order-ul").empty();
				 orders_res = $.data(cacheobj,$("#dropdownMenu3").text());
				 $("#modal-order-ul").append('<li><i class="fa fa-spinner fa-pulse"></i></li>');
				 if (typeof (orders_res)  == "undefined"){
					 $.ajax(
						 {
							 url:"http://192.168.0.108:5050/orders",
							 type:"GET",
							 context:"",
							 data:{"module_name":$("#dropdownMenu3").text()},
							 async:true,
							 success:function(data){
								 orders_length = data["orders_name"].length;
								 if (JSON.stringify(data["orders_name"]) == "[]"){
								 	 $("#modal-order-ul").empty();
									 $("#modal-order-ul").append('<li><a href="#" class="specific_module1">暂无数据...</a></li>');
								 }
								 else{
									 //缓存模块下的指令名称
									 $.data(cacheobj,$("#dropdownMenu3").text(),data["orders_name"]);
									 //清理等待数据
									 $("#modal-order-ul").empty();
									 $.each(data["orders_name"],function (key,value) {
									 	 
										 $("#modal-order-ul").append('<li><a href="#" class="modal-specific-order">'+ value +'</a></li>');
									 })
								 }

							 },
							 error:function (error) {
								 console.error(error);
								 $("#modal-order-ul").empty();
								 $("#modal-order-ul").append('<li><span>暂无数据...</span></li>');
							 }
						 }
					 )
				 }
				 else{
				 	 //清理等待数据
				 	 $("#modal-order-ul").empty();
					 $.each(orders_res,function (key,value) {
					 	 
						 $("#modal-order-ul").append('<li><a href="#" class="modal-specific-order">'+ value +'</a></li>');
					 })
				 }
			});
			
			//选中模态框中的指令
			$("#modal-order-ul").on("click",".modal-specific-order", function() {
				 $("#dropdownMenu4").text($(this).text());
				 $("#dropdownMenu4").append('<span class="caret"></span>');
				 	var params_res = "";
					$("#modal-main,.modal-foot-btn").empty();

					$("#modal-main").append('<div class="initial-condition-title" \
																style="display:none;border-bottom:1px dashed lightgrey;padding-bottom:3px;">\
																<p style="font-size:17px;color:lightgrey">测试用例初始化</p></div>')
                    //标题动画
                    $("#modal-main .initial-condition-title").fadeIn("slow")
					$("#modal-main").append('\
						<div class="modal-main-content">\
							<form class="initial-condition" style="display:block">\
								<div class="input-group input-group">\
								<span class="input-group-addon" id="sizing-addon3">测试用例名称:</span>\
		  						<input type="text" name="test_case" class="form-control tescase-input initial-input" placeholder="TestCaseName" aria-describedby="sizing-addon1">\
								</div>\
								<div class="input-group input-group comment-input-group">\
								<span class="input-group-addon" id="sizing-addon3">备注:</span>\
		  						<input type="text" name="comment" class="form-control comment-input initial-input" placeholder="comments" aria-describedby="sizing-addon1" value="">\
								</div>\
								<div class="input-group input-group author-input-group">\
								<span class="input-group-addon" id="sizing-addon3">编写者:</span>\
		  						<input type="text" name="designer" class="form-control author-input initial-input" placeholder="author" aria-describedby="sizing-addon1" value="">\
								</div>\
							</form>\
						</div>');
					$(".modal-foot-btn").append('<button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button> \
													<button type="button " class="btn btn-info first-next-step">下一步</button>')
					// params_res = $.data(cacheobj,'modal-params');





					// if (typeof (params_res)  == "undefined"){
						$.ajax(
							{
								url:"http://192.168.0.108:5050/params",
								type:"GET",
								context:"",
								data:{"module_name":$("#dropdownMenu3").text(),"order_name":$("#dropdownMenu4").text()},
								async:true,
								success: function(data){
									//$.data(cacheobj,'modal-params',[data["prepose_parameter"],data["test_parameter"],data["bh_parameter"]]);
									//生成前置条件DOM
									if (JSON.stringify(data["prepose_parameter"]) != "null"){
										//生成#modal-main，modal-foot-btn的dom
										//待编写
										};

									//生成测试条件DOM
									if (JSON.stringify(data["test_parameter"]["parameters"]) != "[]"){
										//生成#modal-main，modal-foot-btn的dom
											console.log(data["test_parameter"]["parameters"]);
											$("#modal-main .modal-main-content").before('<div class="modal-main-content-test-parameter-title"\
									          style="display:none;border-bottom:1px dashed lightgrey;padding-bottom:3px;"><p style="font-size:17px; color:lightgrey">测试数据配置</p></div>')

											$("#modal-main .modal-main-content").append('<form class="modal-main-content-test-parameter" style="display:none"></form>')

											$.each(data["test_parameter"]["parameters"],function(key,value){

												if(value["parameter_type"] == "text"){

													$("#modal-main .modal-main-content .modal-main-content-test-parameter").append('<div class="input-group input-group interval-top-10">\
															<span class="input-group-addon" id="sizing-addon3">'+value["parameter_name_chn"]+':</span>\
	  														<input type="text" name="'+value["parameter_name"]+'"class="form-control param-input" placeholder="输入测试数据..." aria-describedby="sizing-addon1">\
	  														</div>'
	  												)
											}
										});
											$(".modal-main-content-test-parameter").append('<div class="input-group input-group interval-top-10">\
															<span class="input-group-addon" id="sizing-addon3">'+"预期结果:"+'</span>\
	  														<input type="text" name="expectval" class="form-control param-input" placeholder="输入预期结果..." aria-describedby="sizing-addon1">\
															</div>');
										
									};

									//生成后置条件DOM
									if(JSON.stringify(data["bh_parameter"]) != "null"){

											//待编写
												}
											},

								error: function (error) {
									console.error(error);
									
								}
							})

			});

			//点击第一个下一步
			$(".modal-foot-btn").on("click",".first-next-step",function(){

                    //实现动画效果
                    $(".modal-main-content .initial-condition").fadeOut(3000)
					$(".modal-main-content .initial-condition").css("display","none");
					$(".initial-condition-title").css("display","none");

					//判断前置条件是否存在
					if ($(".modal-main-content-prepose-parameter").length > 0){

						$(".modal-main-content-prepose-parameter").css("display","block");
						$(".modal-foot-btn").empty()
						$(".modal-foot-btn").append('<button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button> \
													<button type="button " class="btn btn-info second-next-step">下一步</button>')
					}
					else {
						//判断测试数据是否存在
						if ($(".modal-main-content-test-parameter").length > 0){

                            $(".modal-main-content-test-parameter-title,.modal-main-content-test-parameter").fadeIn("slow")
							//$(".modal-main-content-test-parameter-title,.modal-main-content-test-parameter").css("display","block");
							$(".modal-foot-btn").empty()
							if($(".modal-main-content-bh-parameter").length>0 ){

								$(".modal-foot-btn").append('<button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button> \
														<button type="button " class="btn btn-info thrid-next-step">下一步</button>')
							}
							else{
								$(".modal-foot-btn").append('<button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button> \
														<button type="button " class="btn btn-info commit-data">提交</button>')
							}

							
						}
				}



			});
			//点击第二个下一步
			$(".modal-foot-btn").on("click",".second-next-step",function(){

				//置空前置条件
				$(".modal-main-content .modal-main-content-prepose-parameter").css("display","none");

				//显示测试条件
				$(".modal-main-content-test-parameter").css("display","block");
				$(".modal-foot-btn").empty()
				if($(".modal-main-content-bh-parameter").length>0 ){

							$(".modal-foot-btn").append('<button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button> \
													<button type="button " class="btn btn-info thrid-next-step">下一步</button>')
						}
				else{
					$(".modal-foot-btn").append('<button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button> \
													<button type="button " class="btn btn-info commit-data">提交</button>')
				}

					
			});

			//点击第三个下一步
			$(".modal-foot-btn").on("click",".second-next-step",function(){

				//置空后置条件
				$(".modal-main-content .modal-main-content-test-parameter").css("display","none");

				//显示测试条件
				$(".modal-main-content-test-parameter").css("display","block");
				$(".modal-foot-btn").empty()
						
				$(".modal-foot-btn").append('<button type="button" class="btn btn-primary" data-dismiss="modal">关闭</button> \
													<button type="button " class="btn btn-info commit-data">提交</button>')
			});

			//提交数据
			$(".modal-foot-btn").on("click",".commit-data",function(){
				var commit_data = {};
				var parameter_array= new Array();
				// 处理初始化数据
				$(".initial-condition input").each(function(index){

					commit_data[$(this).attr("name")] = $(this).val();
				})

				console.log(commit_data);
				//处理前置数据
				if($(".modal-main-content-prepose-parameter").length > 0 ){
					//待编写
				}

				//处理测试数据
				if($(".modal-main-content-test-parameter").length > 0 ){

					$(".modal-main-content-test-parameter input").each(function(){
						var temp_dict = {};
						temp_dict [$(this).attr("name")] = $(this).val();
						parameter_array.push(temp_dict)
					})
					commit_data["test_parameter"] = parameter_array;


				}
				//处理后置数据
				if($(".modal-main-content-bh-parameter").length > 0 ){
					//待编写
				}

				//上传指令和模块名
				commit_data["order_name"] = $("#dropdownMenu4").text();
				commit_data["module_name"] = $("#dropdownMenu3").text();
				console.log(JSON.stringify(commit_data));
				$.ajax({
					url:"http://192.168.0.108:5050/testcase",
					headers:{
						'Accept': 'application/json',
        				'Content-Type': 'application/json'
					},
					type:"POST",
					context:"",
					data:JSON.stringify(commit_data),
					async:true,
					success: function(){
                        $(".alert2").fadeIn().css("class","alert-success");
						$(".alert2 strong").text("提交成功!");
                        setTimeout(function () { $(".alert2").fadeOut(3000);}, 5000);
                        setTimeout(function () { $("#TestCaseModal").modal("hide");}, 12000);


					},
					error: function(err){
						(".alert").fadeIn().css("class","alert-warning");
						$(".alert strong").text("提交失败!");
                        setTimeout(function () { $(".alert").fadeOut(3000);}, 5000);
						console.log(err);
					}

				})

			});
			$(".search-btn").on("click",function(){

			})
				
})