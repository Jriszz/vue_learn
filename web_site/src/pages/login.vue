<template>
		<div class='background'>
			<div class='login_form'>
					<p>登录</p>
					<el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="70px" class="demo-ruleForm form">
					  <el-form-item label="用户名" prop="user_name">
					    <el-input  v-bind:value="ruleForm.user_name" v-model="ruleForm.user_name" autocomplete="off"></el-input>
					  </el-form-item>
					  <el-form-item label="密码" prop="password">
					    <el-input type="password" v-model="ruleForm.password"></el-input>
					  </el-form-item>
					  <el-form-item>
					    <el-button class='' @click="submitForm('ruleForm')">提交</el-button>
					  </el-form-item>
					</el-form>
			</div>
		</div>
		</el-container>
</template>

<script>
  export default {
    data() {
      var checklength = (rule, value, callback) => {
        setTimeout(() => {
            if (value.length > 18) {
              callback(new Error("字符长度不超过18"));
            } else if (value == '') {
              callback(new Error("不能为空"));
            } 
             else {
              callback();
            }
        }, 1000);
      };
      return {
        ruleForm: {
          user_name: '用户名',
          password: ''
        },
        rules: {
          user_name: [
            { validator: checklength, trigger: 'blur', required: true }
          ],
          password: [
            { validator: checklength, trigger: 'blur', required: true }
          ]
        }
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>

<style type="text/css">
	@import '../style/common.css';
	.background{
		background: url('../assets/img/login.jpg');
		background-size:cover;
		position: fixed;
		top:0;
		width: 100%;
		height: 100%;
	}
	.login_form{
		height: 200px;
		width: 500px;
		margin-left:30%;
		padding: 30px;
		padding-left: 0;
		margin-top: 15%;
		background:rgba(96, 71, 55, 0.5);

	}
	.login_form p{
		margin-bottom:30px;
		margin-left:10px;
		font-size: 30px;
	}

	
</style>