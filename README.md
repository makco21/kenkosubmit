我的程序中出现了这样一个错误，是什么问题。
jsp应该如何与form中的list对象匹配
org.springframework.web.bind.UnsatisfiedServletRequestParameterException: Parameter conditions "SA4G03BG002V010E001, SA4G03BG0023Form" not met for actual request parameters: 
hoseianJouhouItiran[3].hoseianKubun={０１}, 
hoseianJouhouItiran[5].hoseianSyutuganBangou={}, 
hoseianJouhouItiran[8].hoseianHozonFlag={1}, 
hoseianJouhouItiran[6].hoseianRuizigun={01A01}, 
hoseianJouhouItiran[1].hoseianKakunouJunjoBangou={1}, 
hoseianJouhouItiran[0].hoseianRuiCode={０１}, 
hoseianJouhouItiran[2].hoseianSyekMeiNaiyou={化学品シナリオ2}, 
hoseianJouhouItiran[3].hoseianRuiCode={０１}, 
hoseianJouhouItiran[6].hoseianRuiCode={０１}, 
hoseianJouhouItiran[7].hoseianHozonFlag={1},
hoseianJouhouItiran[8].hoseianRuizigun={01A01},

我的浏览器中发送的formdata如下
hoseianJouhouItiran[0]: jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto@2c166b1f
hoseianJouhouItiran[1]: jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto@45a67544
hoseianJouhouItiran[2]: jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto@e4b8599
hoseianJouhouItiran[3]: jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto@28434b34
hoseianJouhouItiran[4]: jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto@371283b0
hoseianJouhouItiran[5]: jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto@41e8cc43
hoseianJouhouItiran[6]: jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto@13ddeeaa
hoseianJouhouItiran[7]: jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto@21751d0e
hoseianJouhouItiran[8]: jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto@2590593
hoseianJouhouItiran[9]: jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto@5d44b4f
hoseianJouhouItiran[0].hoseianSentaku: 
hoseianJouhouItiran[0].hoseianKubun: ０１
hoseianJouhouItiran[0].hoseianRuizigun: 01A01
hoseianJouhouItiran[0].hoseianSiteiSyek: 化学品シナリオ0
hoseianJouhouItiran[0].rokujouSyekKakunouJunjoBangou: 0
hoseianJouhouItiran[0].rokujouGaitouRuiCode: 
hoseianJouhouItiran[0].hoseianKakunouJunjoBangou: 1
hoseianJouhouItiran[0].hoseianRuiCode: ０１
hoseianJouhouItiran[0].hoseianHozonFlag: 1
hoseianJouhouItiran[0].hoseianSyekMeiNaiyou: 化学品シナリオ0
hoseianJouhouItiran[0].hoseianHyouziyouRuizigunCode: 01A01
hoseianJouhouItiran[0].hoseianSyutuganBangou:


自分 が送信しました:
我的form定义如下
/**
     * 補正案情報一覧
     */
    private List<jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto> hoseianJouhouItiran = new ArrayList<jp.go.jpo.sa4g03.domain.service.sr.common.HoseianSetteiJouhouDto>();

public final class HoseianSetteiJouhouDto implements Serializable {

	/**
	 * serialVersionUID
	 */
	private static final long serialVersionUID = 1L;

	/**
	 * Default Constructor.
	 */
	public HoseianSetteiJouhouDto() {

	}

	/**
	 * 補正案選択
	 */
	private String hoseianSentaku = "";

	/**
	 * 補正案区分
	 */
	private String hoseianKubun = "";

	/**
	 * 補正案類似群
	 */
	private String hoseianRuizigun = "";

	/**
	 * 補正案指定商品／役務
	 */
	private String hoseianSiteiSyek = "";

	/**
	 * ６条該当商品役務格納順序番号
	 */
	private long rokujouSyekKakunouJunjoBangou = 0;

	/**
	 * ６条該当類コード
	 */
	private String rokujouGaitouRuiCode = "";

	/**
	 * ６条該当商品役務名内容
	 */
	private String rokujouGaitouSyekMeiNaiyou = "";

	/**
	 * 補正案格納順序番号
	 */
	private long hoseianKakunouJunjoBangou = 0;

	/**
	 * 補正案類コード
	 */
	private String hoseianRuiCode = "";

	/**
	 * 補正案保存フラグ
	 */
	private String hoseianHozonFlag = "";

	/**
	 * 補正案商品役務名内容
	 */
	private String hoseianSyekMeiNaiyou = "";

	/**
	 * 補正案表示用類似群コード
	 */
	private String hoseianHyouziyouRuizigunCode = "";

	/**
	 * 補正案出願番号
	 */
	private String hoseianSyutuganBangou = "";
