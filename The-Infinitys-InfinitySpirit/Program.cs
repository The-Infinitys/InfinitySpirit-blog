// The Infinity's Infinity Style Static Site Generator
using System;
using System.IO;
using System.Text.Json;

Console.WriteLine("-------Infinity Style Static Site Generator-------");
List<string> folderList = GetFolderNames(Environment.CurrentDirectory);
bool isReleaseMode;
isReleaseMode = folderList.Contains("The-Infinitys-InfinitySpirit");
if (isReleaseMode)
{
  Console.WriteLine("Found The-Infinitys-InfinitySpirit. It is release mode");
}
else
{
  Console.WriteLine("Not Found The-Infinitys-InfinitySpiirt. It is test mode");
}

List<string> GetFolderNames(string currentDirectory)
{
  List<string> folderNames = new List<string>();

  foreach (var directory in Directory.EnumerateDirectories(currentDirectory))
  {
    folderNames.Add(Path.GetFileName(directory));
  }

  return folderNames;
}
List<string> GetFileNames(string currentDirectory)
{
  List<string> folderNames = new List<string>();

  foreach (var directory in Directory.EnumerateDirectories(currentDirectory))
  {
    folderNames.Add(Path.GetFileName(directory));
  }

  return folderNames;

}
GetFileNames(Environment.CurrentDirectory);
InfinityStyle.ReadSettingData(isReleaseMode);
Console.WriteLine(InfinityStyle.ConvertMarkdownToHTML(@"# Hello!
THIS IS TEST
## Hello!
THIS IS TEST
### Hello!
THIS IS TEST
#### Hello!
THIS IS TEST
##### Hello!
THIS IS TEST
###### Hello!
THIS IS TEST
"));

// クラス等の用意
public struct htmlTemp
{
  private htmlTemp(string head, string foot)
  {
    head = "";
    foot = "";
  }
}

public class SettingData
{
  public bool isAutoDate { get; set; }
  public int CustomDateYear { get; set; }
  public int CustomDateMonth { get; set; }
  public string? RepositoryName { get; set; }
  public int RepositoryYear { get; set; }
}
public static class ConvertSetting
{
  public static int convertYear;
  public static int convertMonth;
}

public static class InfinityStyle
{
  public static SettingData? settingData;
  public static void ReadSettingData(bool isRelease)
  {
    StreamReader settingJsonFile;
    if (isRelease)
    {
      settingJsonFile = new StreamReader("./The-Infinitys-InfinitySpirit/setting/setting.json");
    }
    else
    {
      settingJsonFile = new StreamReader("./setting/setting.json");
    }
    string settingJsonText = settingJsonFile.ReadToEnd();
    Console.WriteLine("Read setting.json:\n\"\"\"\n" + settingJsonText + "\n\"\"\"");
    settingData = JsonSerializer.Deserialize<SettingData>(
        settingJsonText
    );
    Console.WriteLine("--------------------");
    Console.WriteLine("Read Setting Data");
    Console.WriteLine("--------------------");
    Console.WriteLine("Repository Name: " + settingData?.RepositoryName);
    Console.WriteLine("Repository Year: " + settingData?.RepositoryYear);
    bool isAutoDate;
    if (settingData is not null)
    {
      isAutoDate = settingData.isAutoDate == true;
    }
    else
    {
      isAutoDate = true;
    }
    if (isAutoDate)
    {
      DateTime dt = DateTime.Now;
      ConvertSetting.convertYear = dt.Year;
      ConvertSetting.convertMonth = dt.Month;
    }
    else
    {
      if (settingData?.CustomDateMonth is not null && settingData?.CustomDateYear is not null)
      {
        ConvertSetting.convertYear = settingData.CustomDateYear;
        ConvertSetting.convertMonth = settingData.CustomDateMonth;
      }
      else
      {
        DateTime dt = DateTime.Now;
        ConvertSetting.convertYear = dt.Year;
        ConvertSetting.convertMonth = dt.Month;
      }
    }
    Console.WriteLine("CustomDate Info:");
    Console.WriteLine("Convert Year: " + ConvertSetting.convertYear.ToString());
    Console.WriteLine("Convert Month: " + ConvertSetting.convertMonth.ToString());
    Console.WriteLine("--------------------");
  }
  public static string ConvertMarkdownToHTML(string markdown)
  {
    string[] lines;
    string result = "";
    lines = markdown.Split("\n");
    bool mode_p = false;
    bool mode_code = false;
    for (int i = 0; i < lines.Length; i++)
    {
      string line = lines[i];
      if (mode_code)
      {
        if (line.StartsWith("```"))
        {
          mode_code = false;
          result += "</pre>\n";
        }
        else
        {
          // result+="<code>"+line.Replace("","")+"</code>";
        }

      }
      else
      {
        bool converted = false;
        for (int j = 0; j < 6; ++j)
        {
          if (line.StartsWith(new String('#', j + 1) + " "))
          {
            if (mode_p)
            {
              result += "</p>\n";
              mode_p = !mode_p;
            }
            string innertext = line.Substring(j + 2, line.Length - j - 3);
            result += "<h" + (j + 1).ToString() + ">";
            result += innertext;
            result += "</h" + (j + 1).ToString() + ">\n";
            j = 6;  // 強制終了
            converted = true;
          }
        }
        if (!converted)
        {
          if (line.Replace("\n", "").Replace("\r", "").Length == 0)
          {
            if (mode_p)
            {
              result += "</p>\n";
              mode_p = !mode_p;
            }
            else
            {
              result += "<p></p>";
            }
          }
          else
          {
            if (mode_p)
            {
              result += line.Substring(0, line.Length - 1);
            }
            else
            {
              result += "<p>" + line.Substring(0, line.Length - 1);
              mode_p = !mode_p;
            }
          }
          //ここ直せ
        }
      }
    }
    return result;
  }
}
