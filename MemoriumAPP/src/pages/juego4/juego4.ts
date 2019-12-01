import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { MainPage } from '../';

import { Juego4inPage } from '../juego4in/juego4in';
/**
 * Generated class for the Juego4Page page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-juego4',
  templateUrl: 'juego4.html',
})
export class Juego4Page {

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Juego4Page');
  }
  goGame() {
  	this.navCtrl.push(Juego4inPage);
  }

}
