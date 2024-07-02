# kenkosubmit
健康報告提出プログラム

##　自動として健康報告提出します。
/*
 * @(#)Sa4g03bg0023_SyoruiKanriTDtoRepository.java
 */
package jp.go.jpo.sa4g03.domain.repository.sa4g03bg0023;

import java.util.List;

import org.apache.ibatis.annotations.Param;

/**
 * 類似群コードテーブル
 */
public interface Sa4g03bg0023_RuijigunCodeTDtoRepository {

    /**
     * 類似群コードテーブルの情報を取得する。<br>
     * 
     * @param ruizigunCodeList 類似群コードリスト
     * @return 類似群コード存在件数
     */
    int Sa4g03bg0023RuizigunCodeTDto_Select0001(
            @Param("ruizigunCodeList") List<String> ruizigunCodeList);

}


<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper
	namespace="jp.go.jpo.sa4g03.domain.repository.sa4g03bg0023.Sa4g03bg0023_RuijigunCodeTDtoRepository">
	<select id="Sa4g03bg0023RuizigunCodeTDto_Select0001" resultType="int">SELECT
			COUNT(ruizigun_code)
		FROM
			ruizigun_code_t
		WHERE
			ruizigun_code IN<foreach item="ruizigunCode" collection="ruizigunCodeList" open="(" separator="," close=")">#{ruizigunCode}</foreach>
	</select>
	
</mapper>
