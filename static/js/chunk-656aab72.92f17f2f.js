(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-656aab72"],{"0ff2":function(t,e,a){},"2b72":function(t,e,a){"use strict";var i=a("0ff2"),n=a.n(i);n.a},"456d":function(t,e,a){var i=a("4bf8"),n=a("0d58");a("5eda")("keys",(function(){return function(t){return n(i(t))}}))},"5eda":function(t,e,a){var i=a("5ca1"),n=a("8378"),o=a("79e5");t.exports=function(t,e){var a=(n.Object||{})[t]||Object[t],r={};r[t]=e(a),i(i.S+i.F*o((function(){a(1)})),"Object",r)}},a9d9:function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"app-container"},[a("div",{staticClass:"search-box"},[a("div",{staticStyle:{display:"inline-block"}},[a("label",{staticStyle:{"font-family":"verdana","font-size":"80%","margin-right":"10px"}},[t._v("时间范围：")]),t._v(" "),a("el-date-picker",{attrs:{"default-time":["12:00:00","12:00:00"],type:"datetimerange","picker-options":t.pickerOptions,"range-separator":"至","start-placeholder":"开始日期","end-placeholder":"结束日期",align:"right"},model:{value:t.dateTimeRange,callback:function(e){t.dateTimeRange=e},expression:"dateTimeRange"}})],1),t._v(" "),a("div",{staticStyle:{display:"inline-block"}},[a("el-input",{staticClass:"input-with-select",attrs:{placeholder:"请输入内容"},model:{value:t.search,callback:function(e){t.search=e},expression:"search"}},[a("el-select",{attrs:{slot:"prepend",placeholder:"请选择"},slot:"prepend",model:{value:t.select,callback:function(e){t.select=e},expression:"select"}},[a("el-option",{attrs:{label:"申请人",value:"user_id"}}),t._v(" "),a("el-option",{attrs:{label:"活动",value:"activity_id"}}),t._v(" "),a("el-option",{attrs:{label:"完成情况",value:"finish_case"}})],1),t._v(" "),a("el-button",{attrs:{slot:"append",type:"primary",icon:"el-icon-search"},on:{click:function(e){return t.SearchList(t.dateTimeRange,t.search,t.select)}},slot:"append"})],1)],1)]),t._v(" "),a("el-divider"),t._v(" "),a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.listLoading,expression:"listLoading"}],attrs:{data:t.searchList.slice((t.currentPage-1)*t.pageSize,t.currentPage*t.pageSize),"row-class-name":t.tableRowClassName,"default-sort":{prop:"application_time",order:"descending"},"element-loading-text":"Loading",border:"",fit:"","highlight-current-row":""}},[a("el-table-column",{attrs:{align:"center",label:"ID",width:"80"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v(t._s(e.$index+1))]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"申请人",width:"200",align:"center",sortable:!0,prop:"user_id"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v(t._s(e.row.user_id))]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"活动ID",align:"center",width:"240",sortable:!0,prop:"activity_id"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(e.row.activity_id))])]}}])}),t._v(" "),a("el-table-column",{attrs:{align:"center",label:"申请时间",width:"240",sortable:!0,prop:"application_time"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("i",{staticClass:"el-icon-time"}),t._v(" "),a("span",[t._v(t._s(e.row.application_time))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"完成情况",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v(t._s(e.row.finish_case))]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"操作",width:"220",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-drawer",{ref:"drawer",attrs:{visible:t.showDrawer,"before-close":t.handleClose,"custom-class":"demo-drawer"},on:{"update:visible":function(e){t.showDrawer=e}}},[a("div",{staticClass:"demo-drawer__content"},[a("el-form",{attrs:{model:t.form}},[a("el-form-item",{attrs:{label:"申请人","label-width":t.formLabelWidth}},[a("el-input",{attrs:{type:"input",autosize:{minRows:1,maxRows:2}},model:{value:t.form.user_id,callback:function(e){t.$set(t.form,"user_id",e)},expression:"form.user_id"}})],1),t._v(" "),a("el-form-item",{attrs:{label:"活动ID","label-width":t.formLabelWidth}},[a("el-input",{attrs:{type:"input",autosize:{minRows:1,maxRows:2}},model:{value:t.form.activity_id,callback:function(e){t.$set(t.form,"activity_id",e)},expression:"form.activity_id"}})],1),t._v(" "),a("el-form-item",{attrs:{label:"申请时间","label-width":t.formLabelWidth}},[a("el-date-picker",{staticStyle:{width:"100%"},attrs:{type:"datetime",placeholder:"选择时间"},model:{value:t.form.application_time,callback:function(e){t.$set(t.form,"application_time",e)},expression:"form.application_time"}})],1),t._v(" "),a("el-form-item",{staticStyle:{"text-align":"left"},attrs:{label:"完成情况","label-width":t.formLabelWidth}},[a("el-input",{model:{value:t.form.finish_case,callback:function(e){t.$set(t.form,"finish_case",e)},expression:"form.finish_case"}})],1),t._v(" "),a("el-form-item",{attrs:{label:"申请内容","label-width":t.formLabelWidth}},[a("el-input",{attrs:{type:"textarea",autosize:{minRows:3,maxRows:5}},model:{value:t.form.application_content,callback:function(e){t.$set(t.form,"application_content",e)},expression:"form.application_content"}})],1),t._v(" "),a("el-form-item",{attrs:{label:"申请材料","label-width":t.formLabelWidth}},[a("el-input",{attrs:{type:"textarea",autosize:{minRows:3,maxRows:5}},model:{value:t.form.application_material,callback:function(e){t.$set(t.form,"application_material",e)},expression:"form.application_material"}})],1),t._v(" "),a("el-form-item",{staticStyle:{"text-align":"left"},attrs:{label:"是否通过","label-width":t.formLabelWidth}},[a("el-select",{model:{value:t.form.application_state,callback:function(e){t.$set(t.form,"application_state",e)},expression:"form.application_state"}},[a("el-option",{attrs:{label:"审核通过",value:"examined"}}),t._v(" "),a("el-option",{attrs:{label:"申请拒绝",value:"refused"}})],1)],1),t._v(" "),a("el-form-item",{attrs:{label:"批注","label-width":t.formLabelWidth}},[a("el-input",{attrs:{type:"textarea",autosize:{minRows:1,maxRows:3}},model:{value:t.form.note,callback:function(e){t.$set(t.form,"note",e)},expression:"form.note"}})],1)],1),t._v(" "),a("div",{staticClass:"demo-drawer__footer"},[a("el-button",{on:{click:t.cancelForm}},[t._v("取 消")]),t._v(" "),a("el-button",{attrs:{type:"primary",loading:t.loading},on:{click:function(e){return t.$refs.drawer.closeDrawer()}}},[t._v(t._s(t.loading?"提交中 ...":"确 定"))])],1)],1)]),t._v(" "),a("transition",{attrs:{name:"el-zoom-in-center"}},[a("el-button",{attrs:{type:"primary",size:"mini"},on:{click:function(a){return t.selectContent(e.row)}}},[t._v("查看")])],1),t._v(" "),a("span",[a("el-tooltip",{staticClass:"item",attrs:{effect:"dark",content:"删除这一申请表",placement:"top"}},[a("transition",{attrs:{name:"el-zoom-in-center"}},[a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(a){t.dialogVisible=!0,t.form=e.row}}},[t._v("删除")])],1)],1)],1),t._v(" "),a("el-dialog",{attrs:{title:"提示",visible:t.dialogVisible,width:"30%"},on:{"update:visible":function(e){t.dialogVisible=e}}},[a("span",[t._v("确认永久删除该申请表吗？")]),t._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(e){t.dialogVisible=!1}}},[t._v("取 消")]),t._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:function(e){return t.handleDelete(t.form)}}},[t._v("确 定")])],1)])]}}])})],1),t._v(" "),a("div",{staticClass:"paginationClass"},[a("el-pagination",{attrs:{background:"","hide-on-single-page":!0,"current-page":t.currentPage,"page-sizes":[10,20,50,100],"page-size":t.pageSize,layout:"total, sizes, prev, pager, next, jumper",total:t.total},on:{"size-change":t.handleSizeChange,"current-change":t.handleCurrentChange}})],1)],1)},n=[],o=(a("ac6a"),a("456d"),a("ad8f")),r={filters:{statusFilter:function(t){var e={complete:"success",draft:"gray",deleted:"danger"};return e[t]}},data:function(){return{dateTimeRange:[],beginDate:"",endDate:"",search:"",select:"",dialogVisible:!1,list:null,searchList:null,listLoading:!0,total:0,currentPage:1,pageSize:10,showDrawer:!1,loading:!1,form:{user_id:"",activity_id:"",itable_id:"",application_time:"",finish_case:"",application_content:"",application_material:"",application_state:"",note:""},formLabelWidth:"80px",timer:null,pickerOptions:{shortcuts:[{text:"最近一天",onClick:function(t){var e=new Date,a=new Date;a.setTime(a.getTime()-864e5),t.$emit("pick",[a,e])}},{text:"最近一周",onClick:function(t){var e=new Date,a=new Date;a.setTime(a.getTime()-6048e5),t.$emit("pick",[a,e])}},{text:"最近一个月",onClick:function(t){var e=new Date,a=new Date;a.setTime(a.getTime()-2592e6),t.$emit("pick",[a,e])}},{text:"最近三个月",onClick:function(t){var e=new Date,a=new Date;a.setTime(a.getTime()-7776e6),t.$emit("pick",[a,e])}}]}}},watch:{dateTimeRange:function(t){this.searchList=this.searchList.filter((function(e){return!!t&&(e[2]>=t[0].toLocaleString()&&e[2]<=t[1].toLocaleString()&&(console.log(t[0].toLocaleString()),!0))}))}},created:function(){this.fetchData()},methods:{fetchData:function(){var t=this;this.listLoading=!0,Object(o["l"])().then((function(e){t.list=e.data.items,t.searchList=e.data.items,t.total=e.data.total,t.listLoading=!1})),this.currentChangePage(this.list,this.currentPage)},handleSizeChange:function(t){this.pageSize=t},handleCurrentChange:function(t){this.currentPage=t},selectContent:function(t){this.showDrawer=!0,this.form=t},handleDelete:function(t){var e=this;this.dialogVisible=!1,Object(o["n"])(t).then((function(t){Object(o["l"])().then((function(t){e.list=t.data.items,e.total=t.data.total}))}))},handleClose:function(){var t=this;this.loading||this.$confirm("确定要提交表单吗？").then((function(e){t.loading=!0,t.timer=setTimeout((function(){Object(o["o"])(t.form).then((function(e){Object(o["l"])().then((function(e){t.list=e.data.items,t.total=e.data.total}))})),setTimeout((function(){t.loading=!1}),400)}),2e3)})).catch((function(t){}))},cancelForm:function(){this.loading=!1,this.showDrawer=!1,clearTimeout(this.timer)},SearchList:function(t,e,a){this.searchList=this.searchList.filter((function(t){return Object.keys(t).some((function(i){return String(t[a]).toLowerCase().indexOf(e)>-1}))}))},tableRowClassName:function(t){var e=t.row;return"draft"===e.application_state?"warning-row":"examined"===e.application_state?"success-row":""}}},l=r,s=(a("2b72"),a("2877")),c=Object(s["a"])(l,i,n,!1,null,null,null);e["default"]=c.exports},ad8f:function(t,e,a){"use strict";a.d(e,"l",(function(){return n})),a.d(e,"n",(function(){return o})),a.d(e,"o",(function(){return r})),a.d(e,"i",(function(){return l})),a.d(e,"b",(function(){return s})),a.d(e,"a",(function(){return c})),a.d(e,"k",(function(){return u})),a.d(e,"f",(function(){return d})),a.d(e,"e",(function(){return f})),a.d(e,"m",(function(){return p})),a.d(e,"h",(function(){return m})),a.d(e,"g",(function(){return h})),a.d(e,"j",(function(){return b})),a.d(e,"d",(function(){return _})),a.d(e,"c",(function(){return v}));var i=a("b775");function n(t){return Object(i["a"])({url:"/score/applylist",method:"get",params:t})}function o(t){return Object(i["a"])({url:"/scoreapply/delete",method:"post",data:t})}function r(t){return Object(i["a"])({url:"/scoreapply/update",method:"post",data:t})}function l(t){return Object(i["a"])({url:"/activity/list",method:"get",params:t})}function s(t){return Object(i["a"])({url:"/activity/update",method:"post",data:t})}function c(t){return Object(i["a"])({url:"/activity/delete",method:"post",data:t})}function u(t){return Object(i["a"])({url:"/production/list",method:"get",params:t})}function d(t){return Object(i["a"])({url:"/production/update",method:"post",data:t})}function f(t){return Object(i["a"])({url:"/production/delete",method:"post",data:t})}function p(t){return Object(i["a"])({url:"/student/list",method:"get",params:t})}function m(t){return Object(i["a"])({url:"/student/update",method:"post",data:t})}function h(t){return Object(i["a"])({url:"/student/delete",method:"post",data:t})}function b(t){return Object(i["a"])({url:"/business/list",method:"get",params:t})}function _(t){return Object(i["a"])({url:"/business/update",method:"post",data:t})}function v(t){return Object(i["a"])({url:"/business/delete",method:"post",data:t})}}}]);