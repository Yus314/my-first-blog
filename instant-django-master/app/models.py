from django.db import models

from users.models import User


class Item(models.Model):


            # 自己設定 1　プレイヤー
    element_player_choice = (
        (1, '柿沼祐介'),
        (2, '楠一馬'),
        (3, '窪添永遠'),
    )

    element_1 = models.IntegerField(
        verbose_name='プレイヤー1',
        choices=element_player_choice,
        blank=True,
        null=True,
    )
     # 自己設定 2 キャラ 1
    element_char_kaki = (
        (1, 'ディーディーコング'),
        (2, 'シュルク'),
    )
    element_char_kazu = (
        (1, 'しずえ'),
        (2, 'ホムラ＆ヒカリ'),
        (3, 'キングクルール'),

    )
    element_char_towa = (
        (1, 'カズヤ'),
        (2, 'パックマン'),
        (3, 'ガノンドロフ'),
    )

    element_2 = models.IntegerField(
        verbose_name='キャラ1',
        choices=element_char_kaki,
        blank=True,
        null=True,
    )
    # 自己設定3　プレイヤー2
    element_3 = models.IntegerField(
        verbose_name='プレイヤー2',
        choices=element_player_choice,
        blank=True,
        null=True,
    )

    # 自己設定 4 キャラ 2

    element_4 = models.IntegerField(
        verbose_name='キャラ2',
        choices=element_char_towa,
        blank=True,
        null=True,
    )



    # 自己設定　5 ガチ
    element_5 = models.BooleanField(
        verbose_name='ガチ',
        default=False,
    )


        # 自己設定 6 ステージ
    element_stage_choice = (
        (1, '戦場'),
        (2, '終点'),
        (3, 'ポケモンスタジアム2'),
        (4, 'すま村'),
        (5, '村と街'),
        (6, 'カロスポケモンリーグ'),
        (7, '小戦場'),
    )

    element_6 = models.IntegerField(
        verbose_name='ステージ',
        choices=element_stage_choice,
        blank=True,
        null=True,
    )

    # 自己設定 7　勝者
    element_winner_choice = (
        (1, 'プレイヤー1'),
        (2, 'プレイヤー2'),
    )

    element_7 = models.IntegerField(
        verbose_name='勝者',
        choices=element_winner_choice,
        blank=True,
        null=True,
    )
        # 自己設定 7　じゃんけん勝者
    element_winner_choice = (
        (1, 'プレイヤー1'),
        (2, 'プレイヤー2'),
    )

    element_7 = models.IntegerField(
        verbose_name='じゃんけん勝者',
        choices=element_winner_choice,
        blank=True,
        null=True,
    )


    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.sample_1

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
