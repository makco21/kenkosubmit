# kenkosubmit
健康報告提出プログラム

##　自動として健康報告提出します。
<form:form
					action="${pageContext.request.contextPath}/SA4G03BG00203/ver1/SA4G03BG002V010F001"
					id="hoseianSeiteiForm" method="post"
					modelAttribute="SA4G03BG0023Form" style="width: 1030px;">
<div class="grid-container util-mb-20px util-mt-20px util-mr-0px">
											<div class="grid-container-item util-pt-5px ">
												<span style="display: inline-block; width: 130px;">区分</span><span
													class="util-ml-10px util-mr-10px">：</span>
											</div>
											<div class="grid-container-item util-mt-5px" id="kubun1">${f:h(SA4G03BG0023Form.hoseianKubun)}
												</div>
										</div>
										<div class="grid-container util-mb-20px ">
											<div class="grid-container-item util-pt-5px">
												<span style="display: inline-block; width: 130px;">類似群</span><span
													style="margin-left: 10px; margin-right: 15px;">：</span>
											</div>
											<div class="grid-container-item util-mt-5px f"
												style="width: 702px;" id="rujigun1">${f:h(SA4G03BG0023Form.hoseianRuizigun)}
												</div>
										</div>
										<div class="grid-container util-mb-20px ">
											<div class="grid-container-item util-pt-5px">
												<span style="display: inline-block; width: 130px;">指定商品／役務</span><span
													class="util-ml-10px util-mr-15px">：</span>
											</div>
											<div class="grid-container-item util-mt-5px"
												style="width: 700px; white-space: pre-wrap;"
												id="siteiSyouhinEkimu1">${f:h(SA4G03BG0023Form.hoseianSiteiSyek)}
											</div>
										</div>
</form:form>

 @RequestMapping(value = "SA4G03BG002V010F001", method = { RequestMethod.POST }, params = {
            "SA4G03BG002V010E001", "SA4G03BG0023Form" })
    @ResponseBody
    public String sA4G03BG002C054(@ModelAttribute("SA4G03BG0023Form") SA4G03BG0023Form form,
            Model model) {...}
