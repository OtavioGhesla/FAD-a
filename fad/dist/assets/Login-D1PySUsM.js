import{B as c}from"./Back-DPqJhWKa.js";import{_ as w,c as t,a as e,w as v,b as f,d,v as l,t as m,e as u,o as n,r as g}from"./index-B0CyqVYp.js";const h={name:"Login",components:{Back:c},data(){return{name:"",password:"",errorName:"",errorPassword:""}},methods:{submitForm(){if(this.errorName=this.name?"":"Seu nome de usuário deve ter pelo menos uma letra",this.errorPassword=this.password?"":"Senha incorreta",this.errorName||this.errorPassword)return;const i=JSON.stringify({name:this.name,password:this.password});console.log(i)}}},N={class:"login-page"},b={class:"container",id:"um"},_={class:"input-name"},k={key:0,class:"error"},y={class:"input-password"},B={key:1,class:"error"};function S(i,s,x,F,o,a){const p=g("Back");return n(),t("div",N,[e("div",b,[e("form",{class:"interface",onSubmit:s[2]||(s[2]=v((...r)=>a.submitForm&&a.submitForm(...r),["prevent"]))},[f(p),s[5]||(s[5]=e("h1",null,"Faça seu log in",-1)),e("div",_,[s[3]||(s[3]=e("h3",null,"Nome",-1)),d(e("input",{class:"name",type:"text",placeholder:"Insira seu nome de usuário","onUpdate:modelValue":s[0]||(s[0]=r=>o.name=r)},null,512),[[l,o.name]])]),o.errorName?(n(),t("div",k,m(o.errorName),1)):u("",!0),e("div",y,[s[4]||(s[4]=e("h3",null,"Senha",-1)),d(e("input",{class:"password",type:"password",placeholder:"Insira sua senha","onUpdate:modelValue":s[1]||(s[1]=r=>o.password=r)},null,512),[[l,o.password]])]),o.errorPassword?(n(),t("div",B,m(o.errorPassword),1)):u("",!0),s[6]||(s[6]=e("div",{class:"input-submit"},[e("input",{class:"submit",type:"submit",value:"Fazer Sign up"})],-1))],32)]),s[7]||(s[7]=e("div",{class:"container",id:"dois"},null,-1))])}const I=w(h,[["render",S],["__scopeId","data-v-05490ba7"]]);export{I as default};
